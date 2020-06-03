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
parser.add_argument('--scale_factor', type=float, default=1.0)
parser.add_argument('--notxt', action='store_true')
parser.add_argument('--image_dir', type=str, default='./images')
parser.add_argument('--output_dir', type=str, default='./output')
args = parser.parse_args()




class Similarity():
    def __init__(self):
        # initialize PoseNet Model
        print("[INFO] loading PoseNet Model...")
        argument_model=101
        self.output_scale=1
        self.model=posenet.load_model(argument_model).cuda()
        self.output_stride = self.model.output_stride
        self.Pose_pattern = np.loadtxt('golden_pattern.txt', delimiter=' ')

    def predict(self,input_image):
        start = time.time()
        with torch.no_grad(): 
            input_image = torch.Tensor(input_image).cuda()

            heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = self.model(input_image)

            pose_scores, keypoint_scores, keypoint_coords = self.model.decode_multiple_poses(
                heatmaps_result.squeeze(0),
                offsets_result.squeeze(0),
                displacement_fwd_result.squeeze(0),
                displacement_bwd_result.squeeze(0),
                output_stride=self.output_stride,
                max_pose_detections=1,#TODO
                min_pose_score=0.25)
        keypoint_coords *= self.output_scale 
        print("keypoint_coords")
        for pi in range(len(pose_scores)):
            if pose_scores[pi] == 0.:
                break
            print('Pose #%d, score = %f' % (pi, pose_scores[pi]))
            for ki, (s, c) in enumerate(zip(keypoint_scores[pi, :], keypoint_coords[pi, :, :])):
                print('Keypoint %s, score = %f, coord = %s' % (posenet.PART_NAMES[ki], s, c))
        print('Average FPS:', 1 / (time.time() - start))

        return keypoint_coords #return max_pose_detections*17*2 np.array

    def pose_dance(self, input_image): 
        #=====
        # data_type
        # target      : img
        # Pose_mission: List[]
        #=====one time pass multiple pose=====
        input_image=self.predict(input_image)
        input_image=self.transform(input_image)
        for i in range(1,self.Pose_pattern.shape[0]):
            result , Eu_dist =self.Pose_similarity(input_image,self.Pose_pattern[i,:])
            if result :
                return i,Eu_dist #return pose id
        return -1 #nothing match 
            


        
    def Pose_similarity(self,Input,Pose_pattern):
        #===Data type===
        # Input       :1x34 list
        # Pose_pattern:1x34 list
        # Threshold   :check whether it's similar?
        Threshold=0.2 #TODO
        cos_sim= np.dot(Input,Pose_pattern)/( np.linalg.norm(Input)*np.linalg.norm(Pose_pattern) )
        Eu_dist=np.sqrt(2*(1-cos_sim))
        print("Cos simalarity",cos_sim)
        print("Euclidean_dist",Eu_dist)

        result = Eu_dist<=Threshold # True is similar
        return result , Eu_dist

    def transform(self,input):
        input=input.reshape(17,2)
        max=input.max(axis=0)
        min=input.min(axis=0)
        return ( (input-min)/(max-min) ).reshape(34,1)


if __name__ == "__main__":
    sim=Similarity()

    if args.output_dir:
        if not os.path.exists(args.output_dir):
            os.makedirs(args.output_dir)

    filenames = [f.path for f in os.scandir(args.image_dir) if f.is_file() and f.path.endswith(('.png', '.jpg'))]
    for f in filenames:
        print("Pose_ID:",sim.pose_dance(f))





