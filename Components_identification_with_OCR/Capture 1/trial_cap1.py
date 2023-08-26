import pyrealsense2 as rs
import numpy as np
import cv2
import rtde_control
import easyocr
import matplotlib.pyplot as plt
import openpyxl
import time
import points as p
from statistics import mode
import re

import rtde_control
import rtde_receive
rtde_r = rtde_receive.RTDEReceiveInterface("169.254.37.182")
rtde_c = rtde_control.RTDEControlInterface("169.254.37.182")
# Parameters
velocity = 0.5
acceleration = 0.5
dt = 1.0/500  # 2ms
lookahead_time = 0.1
gain = 300

result_f={}
depth_dict={}
## dest_dict={}#########################################################################
# rtde_c = rtde_control.RTDEControlInterface("169.254.37.182")
rtde_c.moveL([-0.30898, -0.64203, 0.19003, 0.032, -3.154, -0.017], 0.5, 0.3) #Capturing position
time.sleep(1)
num=p.point()
print(num)

def depth_filter(win_data):
    x1,y1,x2,y2=win_data[0]-win_data[2]/2,win_data[1]-win_data[3]/2,win_data[0]+3*win_data[2]/2,win_data[1]+3*win_data[3]/2
    for i in range(int(y1),int(y2)):
        for j in range(int(x1),int(x2)):
            d=aligned_depth_frame.get_distance(int(j),int(i))
            if d!=0:
                k=[j,i]
                depth_dict[f'{k}']=round(d, 2)
    depth_list=depth_dict.values()
    filtered_depth=mode(depth_list)
    print(filtered_depth)
    corr_pix=list(depth_dict.keys())[list(depth_dict.values()).index(filtered_depth)] #get corresponding pixel of the distance value
    print(corr_pix)
    print(type(corr_pix))
    #print(corr_pix) #A string here
    corr_pix=re.split(', ',corr_pix)
    pix_corr=[]
    for num in corr_pix:
        num=re.sub(r"[\([{})\]]", "", num)
        num=int(num)
        pix_corr.append(num)
    
    print(pix_corr)
    print(type(pix_corr))
    a,b=pix_corr[0],pix_corr[1]
    depth=aligned_depth_frame.get_distance(int(a),int(b))
    return depth
def distance(x,y):
    #cv2.circle(capture,(x,y),2,(128,0,128),-1)
    #print((x,y))
    d=depth_frame.get_distance(int(x),int(y))
    print(d)
    if (d==0.0) :
        print('No depth info, Using an window')
        depth=depth_filter([int(x),int(y),10,10])
        x_w, y_w, z_w = convert_depth_to_phys_coord_using_realsense(int(x),int(y), depth, camera_info)
        print('Camera Points are:',x_w, y_w, z_w)
        p1=f'{x_w} {y_w} {z_w}'
        p = [float(value) for value in p1.split(' ')]
        p.append(1.0)
        dst_p=np.matmul(k,p)
        dst_p=dst_p.tolist()
        print(dst_p)
        rtde_c.moveL([dst_p[0]/1000.0, dst_p[1]/1000.0, dst_p[2]/1000.0, 0.032, -3.154, -0.017], 0.5, 0.3)
        #time.sleep(5)
        #dst_p=(dst_p[0])[:-1]
        #print(dst_p)
        del p1
        del p
    else:
        x_w, y_w, z_w = convert_depth_to_phys_coord_using_realsense(int(x),int(y), d, camera_info)
        print('Camera Points are:',x_w, y_w, z_w)
        p1=f'{x_w} {y_w} {z_w}'
        p = [float(value) for value in p1.split(' ')]
        p.append(1.0)
        dst_p=np.matmul(k,p)
        dst_p=dst_p.tolist()
        print(dst_p)
        rtde_c.moveL([dst_p[0]/1000.0, dst_p[1]/1000.0, dst_p[2]/1000.0, 0.032, -3.154, -0.017], 0.5, 0.3)
        #time.sleep(5)
        #dst_p=(dst_p[0])[:-1]
        #print(dst_p)
        del p1
        del p

def convert_depth_to_phys_coord_using_realsense(x, y, depth, cameraInfo):
    _intrinsics = rs.intrinsics()
    _intrinsics.width = cameraInfo.width
    _intrinsics.height = cameraInfo.height
    _intrinsics.ppx = cameraInfo.ppx
    _intrinsics.ppy = cameraInfo.ppy
    _intrinsics.fx = cameraInfo.fx
    _intrinsics.fy = cameraInfo.fy
    # _intrinsics.model = cameraInfo.distortion_model
    _intrinsics.model  = rs.distortion.none
    _intrinsics.coeffs = [i for i in cameraInfo.coeffs]
    result = rs.rs2_deproject_pixel_to_point(_intrinsics, [x, y], depth)
    # result[0]: right, result[1]: down, result[2]: forward
    return result[0], -result[1], -result[2]
"""
# Setup the pipeline
pipe = rs.pipeline()
cfg = rs.config()
cfg.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
cfg.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
profile = pipe.start(cfg)
"""

k= [[-724.60538548,82.90733245,285.41238816,-195.72598377],[18.67714179,-740.17953151,41.7580128,-683.01233701],[-84.6609671,44.4134883,-11.45772205,129.27829634],[0,0,0,1]]


# Create a pipeline
pipeline = rs.pipeline()

# Create a config and configure the pipeline to stream
config = rs.config()
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
device_product_line = str(device.get_info(rs.camera_info.product_line))
print(device_product_line)
found_rgb = False
for s in device.sensors:
    if s.get_info(rs.camera_info.name) == 'RGB Camera':
        found_rgb = True
        print("There is a depth camera with color sensor")
        break
if not found_rgb:
    print("The demo requires Depth camera with Color sensor")
    exit(0)
config.enable_stream(rs.stream.depth, 848,480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 848,480, rs.format.bgr8, 30)
profile = pipeline.start(config)


# Setup the 'High Accuracy'-mode
depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)
clipping_distance_in_meters = 0.3 #1 meter
clipping_distance = clipping_distance_in_meters / depth_scale
print(clipping_distance)
preset_range = depth_sensor.get_option_range(rs.option.visual_preset)
for i in range(int(preset_range.max)):
    visulpreset = depth_sensor.get_option_value_description(rs.option.visual_preset,i)
    print('%02d: %s'%(i,visulpreset))
    if visulpreset == "High Accuracy":
        depth_sensor.set_option(rs.option.visual_preset, i)
# enable higher laser-power for better detection
depth_sensor.set_option(rs.option.laser_power, 180)
# lower the depth unit for better accuracy and shorter distance covered
depth_sensor.set_option(rs.option.depth_units, 0.0005)
align_to = rs.stream.color
align = rs.align(align_to)
# Skip first frames for auto-exposure to adjust
for x in range(5):
    pipeline.wait_for_frames()
t1=time.time()
try:
    while True:

        # Stores next frameset
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if color_frame:
            aligned_frames = align.process(frames)

            # Get aligned frames
            aligned_depth_frame = aligned_frames.get_depth_frame() # aligned_depth_frame is a 640x480 depth image
            color_frame = aligned_frames.get_color_frame()

            # Validate that both frames are valid
            if not aligned_depth_frame or not color_frame:
                continue

            depth_image = np.asanyarray(aligned_depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())

            # Remove background - Set pixels further than clipping_distance to grey
            black_color = 0
            depth_image_3d = np.dstack((depth_image,depth_image,depth_image)) #depth image is 1 channel, color is 3 channels
            bg_removed = np.where((depth_image_3d > clipping_distance) | (depth_image_3d <= 0), black_color, color_image)

            # Render images:
            #   depth align to color on left
            #   depth on right
            #depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
            #images = np.hstack((bg_removed, depth_colormap))
            camera_info = aligned_depth_frame.profile.as_video_stream_profile().intrinsics
            t2=time.time()
            if (t2-t1)>3:
                cv2.imwrite('captured.jpg',bg_removed)
                # cv2.imshow('captured',bg_removed)
                # cv2.waitKey(0)
                # # cv2.destroyAllWindows()
                break
                     
    
    # Stop streaming
    rtde_c.disconnect()
    pipeline.stop()