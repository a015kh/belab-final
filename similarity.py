import cv2
import time
import numpy as np
import argparse
import os
import torch
import posenet


#=============================================
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=int, default=101)
parser.add_argument('--scale_factor', type=float, default=0.7125)
parser.add_argument('--notxt', action='store_true')
parser.add_argument('--image_dir', type=str, default='./images_bak')
parser.add_argument('--output_dir', type=str, default='./output')
args = parser.parse_args()




class Similarity():
    def __init__(self):
        # initialize PoseNet Model
        print("[INFO] loading PoseNet Model...")
        argument_model=101
        self.scale_factor=0.7125#TODO image our:0.1
        self.model=posenet.load_model(argument_model).cuda()
        self.output_stride = self.model.output_stride
        self.Pose_pattern = np.loadtxt('golden_pattern.txt', delimiter=' ')
        self.pose_scores =0
        self.keypoint_scores=0
        self.keypoint_coords=None

    def predict(self,input_image, output_scale):
        print("[INFO] Predict Start...")
        start = time.time()
        with torch.no_grad(): 
            input_image = torch.Tensor(input_image).cuda()

            heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = self.model(input_image)

            pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multiple_poses(
                heatmaps_result.squeeze(0),
                offsets_result.squeeze(0),
                displacement_fwd_result.squeeze(0),
                displacement_bwd_result.squeeze(0),
                output_stride=self.output_stride,
                max_pose_detections=1,
                min_pose_score=0.25)
        
        ''' 
        print("keypoint_coords")
        for pi in range(len(pose_scores)):
            if pose_scores[pi] == 0.:
                break
            print('Pose #%d, score = %f' % (pi, pose_scores[pi]))
            for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
                print('Keypoint %s, score = %f, coord = %s' % (posenet.PART_NAMES[ki], s, c))
        
        '''
        #print("FPS",1/(time.time()-start))
        self.pose_scores =pose_scores
        self.keypoint_scores=keypoint_scores
        self.keypoint_coords=keypoint_coords/output_scale 

        return  #keypoint_coords #return max_pose_detections*17*2 np.array

    def pose_dance(self, input_image, output_scale,width): 
        #=====
        # data_type
        # target      : img
        # Pose_mission: List[]
        #=====one time pass multiple pose=====
        #print(input_image)
        self.predict(input_image, output_scale)
        
        input_image=self.transform(self.keypoint_coords)
        pose =[0.3]
        for i in range(1,self.Pose_pattern.shape[0]):
            result , Eu_dist = self.Pose_similarity(input_image,self.Pose_pattern[i,:])
            pose.append( Eu_dist)
        
        #idx from 1~17 7*2+3
        pose=np.argmin(pose)
        col=self.color(width)
        pose_id=pose*3+col-3-1#0~50
        print("Pose",pose,"Location:",col)
        return pose_id #return 0 not match 
            


        
    def Pose_similarity(self,Input,Pose_pattern):
        #===Data type===
        # Input       :1x34 list
        # Pose_pattern:1x34 list
        # Threshold   :check whether it's similar?
        Threshold=0.2 #TODO
        cos_sim= np.dot(Input,Pose_pattern)/(1e-8+np.linalg.norm(Input)*np.linalg.norm(Pose_pattern) )
        Eu_dist=np.sqrt(2*(1-cos_sim+1e-8))
        #print("Cos simalarity",cos_sim,"Euclidean_dist",Eu_dist)

        result = Eu_dist<=Threshold # True is similar
        return result , Eu_dist

    def transform(self,input):
        input=input.reshape(17,2)
        max=input.max(axis=0)
        min=input.min(axis=0)
        return ( (input-min)/(max-min) ).reshape(1,34)
    def write_image(self,filenames):
        for f in filenames:
            input_image, draw_image, output_scale = posenet.read_imgfile(
                f, scale_factor=self.scale_factor, output_stride=self.output_stride)
            print("Pose_ID:",self.pose_dance(input_image,output_scale))
    def write_camera(self):
            cap = cv2.VideoCapture(0)
            cap.set(3, 960)
            cap.set(4, 720)
            while True:
                input_image, display_image, output_scale = posenet.read_cap(cap, scale_factor=self.scale_factor, output_stride=self.output_stride)
                #print("Pose_ID:",sim.pose_dance(input_image,output_scale))
                sim.pose_dance(input_image,output_scale)
                # TODO this isn't particularly fast, use GL for drawing and display someday...
                overlay_image = posenet.draw_skel_and_kp(
                    display_image, self.pose_scores, self.keypoint_scores, self.keypoint_coords,
                min_pose_score=0.15, min_part_score=0.1)

                cv2.imshow('posenet', overlay_image)
                #frame_count += 1
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    def color(self,width):
	#depend on noise location

        
        loc=-1
        
        x_idx=self.keypoint_coords[0,0,1]
        print(x_idx,width)
        if x_idx<=width*1/3   :loc=1
        elif x_idx<=width*2/3 :loc=2
        elif x_idx<=width*3/3 :loc=3
        #print("center loc",loc)
        return loc  	


if __name__ == "__main__":
    sim=Similarity()

    if args.output_dir:
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)

    filenames = [f.path for f in os.scandir(args.image_dir) if f.is_file() and f.path.endswith(('.png', '.jpg'))]
    #sim.write_image(filenames)
    sim.write_camera()
    

