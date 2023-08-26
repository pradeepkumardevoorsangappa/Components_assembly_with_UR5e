import rtde_control
import time
import robotiq_gripper
ip = "  " ###ROBOT IP####
rtde_c = rtde_control.RTDEControlInterface(ip)


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

##PICKING COMPONENT NO.11
print("PICKING COMPONENT NO.11")
rtde_c.moveL([-0.16782,-0.70146,0.38802,0.036,-3.154,-0.017], 0.5, 0.3)
rtde_c.moveL([-0.36783,-0.68956,0.11500,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([-0.36783,-0.68956,0.02500,2.232,2.201,-0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.11
print("PLACING COMPONENT NO.11")
rtde_c.moveL([-0.36785,-0.68958,0.11495,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([-0.36780,-0.57204,0.11500,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([-0.36618,-0.55836,0.008,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([-0.36620,-0.45540,0.008,2.232,2.201,-0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.12
print("PICKING COMPONENT NO.12")
rtde_c.moveL([-0.36617,-0.45550,0.11494,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([0.12492,-0.6895,0.11495,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([0.125,-0.68986,0.02502,2.232,2.201,-0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.12
print("PLACING COMPONENT NO.12")
rtde_c.moveL([0.12496,-0.68984,0.11495,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([0.12502,-0.57734,0.11501,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([0.15167,-0.55967,0.0081,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([0.15162,-0.45803,0.0081,2.232,2.201,-0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.13
print("PICKING COMPONENT NO.13")
rtde_c.moveL([0.15055,-0.4591,0.115,2.232,2.201,-0.005], 0.5, 0.3)
rtde_c.moveL([-0.53246, -0.58505, 0.114994, 2.223, 2.190, -0.018], 0.5, 0.3)
rtde_c.moveL([-0.53250, -0.58502, -0.040002, 2.223, 2.190, -0.018], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.13
print("PLACING COMPONENT NO.13")
rtde_c.moveL([-0.53251, -0.585, 0.11496, 2.223, 2.19, -0.018], 0.5, 0.3)
rtde_c.moveL([-0.27381, -0.45546, 0.04498, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.27383, -0.45555, 0.02471, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.30992, -0.45553, 0.02472, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.14
print("PICKING COMPONENT NO.14")
rtde_c.moveL([-0.31041, -0.45532, 0.11499, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.27967, -0.58801, 0.11500, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.27973, -0.58695, -0.04, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.14
print("PLACING COMPONENT NO.14")
rtde_c.moveL([0.27971, -0.58834, 0.11499, 2.223, 2.190, -0.018], 0.5, 0.3)
rtde_c.moveL([0.05576, -0.45815, 0.04500, 2.239, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.05576, -0.45745, 0.02513, 2.239, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.09360, -0.45744, 0.02512, 2.239, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.15
print("PICKING COMPONENT NO.15")
rtde_c.moveL([0.10016, -0.45815, 0.11500, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.30202, -0.68954, 0.11497, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.30188, -0.68953, 0.01498, 2.231, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.15
print("PLACING COMPONENT NO.15")
rtde_c.moveL([-0.30191, -0.68953, 0.11501, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.25939, -0.45501, 0.11497, 2.231, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.25949, -0.45500, 0.075, 2.231, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.25947, -0.45502, 0.04828, 2.231, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.16
print("PICKING COMPONENT NO.16")
rtde_c.moveL([-0.25949, -0.45500, 0.11499, 2.231, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.06001, -0.68947, 0.11486, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.06003, -0.69148, 0.01501, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.16
print("PLACING COMPONENT NO.16")
rtde_c.moveL([0.05998, -0.69145, 0.11499, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([0.04590, -0.45695, 0.11496, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.04590, -0.45695, 0.06958, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.04588, -0.45700, 0.05001, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.17
print("PICKING COMPONENT NO.17")
rtde_c.moveL([0.045852, -0.45699, 0.11498, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.24000, -0.68952, 0.11493, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.24005, -0.68956, 0.01506, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.17
print("PLACING COMPONENT NO.17")
rtde_c.moveL([-0.24006, -0.68953, 0.11494, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.20832, -0.45488, 0.1150, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.20831, -0.45440, 0.06913, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.20866, -0.45498, 0.05018, 2.231, 2.201, -0.006], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.18
print("PICKING COMPONENT NO.18")
rtde_c.moveL([-0.20860, -0.45487, 0.11499, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([0.00001, -0.68949, 0.114871, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.00001, -0.69094, 0.01500, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.18
print("PLACING COMPONENT NO.18")
rtde_c.moveL([-0.00003, -0.69093, 0.11499, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.005715, -0.45488, 0.11499, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.004772, -0.45662, 0.070, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.00478, -0.45530, 0.050, 2.232, 2.201, -0.004], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.19
print("PICKING COMPONENT NO.19")
rtde_c.moveL([-0.004783, -0.455279, 0.114981, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.18001, -0.689517, 0.11492, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.17998, -0.689543, 0.01506, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.19
print("PLACING COMPONENT NO.19")
rtde_c.moveL([-0.18001, -0.68951, 0.11494, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.158068, -0.45482, 0.11998, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.15806, -0.45481, 0.07502, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.158060, -0.454780, 0.0500072, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.20
print("PICKING COMPONENT NO.20")
rtde_c.moveL([-0.158038, -0.4547909, 0.119986, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.0599926, -0.68948, 0.1149, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.059975, -0.68976, 0.01500, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.20
print("PLACING COMPONENT NO.20")
rtde_c.moveL([-0.05998, -0.68979, 0.11498, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.05987, -0.45481, 0.12000, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.05987, -0.45481, 0.07505, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.0598, -0.45482, 0.05503, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)

##PICKING COMPONENT NO.21
print("PICKING COMPONENT NO.21")
rtde_c.moveL([-0.05981, -0.454730, 0.119993, 2.232, 2.201, -0.004], 0.5, 0.3)
rtde_c.moveL([-0.120001, -0.689490, 0.114911, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.119992, -0.68949, 0.01500, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(224, 255, 255)

##PLACING COMPONENT NO.21
print("PLACING COMPONENT NO.21")
rtde_c.moveL([-0.11999, -0.689529, 0.119996, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.120, -0.57819, 0.115, 2.232, 2.201, -0.005], 0.5, 0.3)
rtde_c.moveL([-0.11993, -0.57819, 0.0, 2.232, 2.201, -0.005], 0.5, 0.3)
gripper.move_and_wait_for_pos(0, 255, 255)
rtde_c.moveL([-0.11993, -0.57819, 0.130, 2.232, 2.201, -0.005], 0.5, 0.3)

rtde_c.disconnect()
