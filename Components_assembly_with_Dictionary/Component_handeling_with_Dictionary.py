import rtde_control
import time
import robotiq_gripper
import point_data as pd
ip = "  "  ####robot ip###
 
def log_info(gripper):
    print(f"Pos: {str(gripper.get_current_position()): >3}  "
          f"Open: {gripper.is_open(): <2}  "
          f"Closed: {gripper.is_closed(): <2}  ")

print("Creating gripper...")
gripper = robotiq_gripper.RobotiqGripper()
print("Connecting to gripper...")
gripper.connect(ip, 63352)
rtde_c = rtde_control.RTDEControlInterface(ip)
print("Activating gripper...")
gripper.activate()
gripper.move_and_wait_for_pos(0, 255, 255)

#Robot Moves to capture position
rtde_c.moveL([-0.16782,-0.70146,0.38802,0.036,-3.154,-0.017], 0.5, 0.3)
source=pd.source_data()
dest=pd.dest_data()

# Robot does the pick and assembly task as per the Dictionary
for i in range(21,22):
    print(f'PICKING COMPONENT NO.{i}')
    for j in range(3):
        rtde_c.moveL(source[i][j], 0.5, 0.3)
    gripper.move_and_wait_for_pos(224, 255, 255)
    print(f'PLACING COMPONENT NO.{i}')
    for k in range(4):
        rtde_c.moveL(dest[i][k], 0.5, 0.3)
    gripper.move_and_wait_for_pos(0, 255, 255)

rtde_c.moveL([-0.11993, -0.57819, 0.130, 2.232, 2.201, -0.005], 0.5, 0.3)    

rtde_c.disconnect()