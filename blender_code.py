import serial
import time
import bpy

ser=serial.Serial('/dev/ttyUSB77','9600')
time.sleep(3)

rolls=[]
pitchs=[]
headings=[]



def SetBoneRotationDeg(human,boneName,rotEulerDeg):
    human.pose.bones[boneName].rotation_mode = 'XYZ'    
    human.pose.bones[boneName].rotation_euler[0] = rotEulerDeg[2]
    human.pose.bones[boneName].rotation_euler[1] = rotEulerDeg[0]
    human.pose.bones[boneName].rotation_euler[2] = rotEulerDeg[1]



data = ser.readline().decode().rstrip()
data = ser.readline().decode().rstrip()
data = ser.readline().decode().rstrip()
data = ser.readline().decode().rstrip()

start=data.find('<')
start+=1
end=data.find('>',start)
output=data[start:end]
val = output.split(';')

winSize = 5


for i in range(0,6):
    data = ser.readline().decode().rstrip()
    val = output.split(';')
    values = val[i].split(',')
    rolls.append(float(values[0]))
    pitchs.append(float(values[1]))
    headings.append(float(values[2]))


for i in range(20000):
        if ser.in_waiting > 0:
            # Read a line of serial data from the Arduino
            
            roll=[]
            pitch=[]
            heading=[]
            
            data = ser.readline().decode().rstrip()
            start=data.find('<')
            start+=1
            end=data.find('>',start)
            output=data[start:end]
            val = output.split(';')
            for i in range(0,6):
                values = val[i].split(',')
                roll.append(float(values[0]))
                pitch.append(float(values[1]))
                heading.append(float(values[2]))
            
# THUMB FINGER
            first_ang = -0.01*(roll[5]-rolls[5]) + 0.01*(roll[0]-rolls[0]) 
            if first_ang < -5:
                    first_ang = -5
            elif first_ang >100:
                first_ang = 100
            mid_ang = 2*first_ang
            last_ang = 3.5*first_ang
            if mid_ang < 0:
                mid_ang = 0
            if last_ang < 0:
                last_ang = 0
            splay_ang = 0.01*(headings[5]-heading[5]) - 0.015*(pitchs[0]-pitch[0])
                
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'T_first',[0,splay_ang, first_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'T_middle',[0,0,mid_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'T_last',[0,0,last_ang])                
                
# INDEX FINGER
            first_ang = 0.01*(headings[1]-heading[1]) - 0.015*(pitchs[0]-pitch[0])
            if first_ang < -10:
                    first_ang = -10
            elif first_ang >150:
                first_ang = 150
            mid_ang = 2*first_ang
            last_ang = 3*first_ang
            if mid_ang < 0:
                mid_ang = 0
            if last_ang < 0:
                last_ang = 0
            splay_ang = -0.01*(roll[1]-rolls[1]) + 0.01*(roll[0]-rolls[0])
            if splay_ang < -15:
                splay_ang = -15
            elif splay_ang >15:
                splay_ang = 15
                
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'I_first',[0,first_ang,splay_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'I_middle',[0,mid_ang,0])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'I_last',[0,last_ang,0])
## MIDDLE FINGER
            first_ang = 0.01*(headings[2]-heading[2]) - 0.017*(pitchs[0]-pitch[0])
            if first_ang < -10:
                    first_ang = -10
            elif first_ang >150:
                first_ang = 150
            mid_ang = 2*first_ang
            last_ang = 3*first_ang
            if mid_ang < 0:
                mid_ang = 0
            if last_ang < 0:
                last_ang = 0
            splay_ang = -0.01*(roll[2]-rolls[2]) + 0.01*(roll[0]-rolls[0])
            if splay_ang < -15:
                splay_ang = -15
            elif splay_ang >15:
                splay_ang = 15
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'M_first',[0,first_ang,splay_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'M_middle',[0,mid_ang,0])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'M_last',[0,last_ang,0])

## RING FINGER
            first_ang = 0.01*(headings[3]-heading[3]) - 0.016*(pitchs[0]-pitch[0])
            if first_ang < -10:
                    first_ang = -10
            elif first_ang >150:
                first_ang = 150
            mid_ang = 2*first_ang
            last_ang = 3*first_ang
            if mid_ang < 0:
                mid_ang = 0
            if last_ang < 0:
                last_ang = 0
            splay_ang = -0.01*(roll[3]-rolls[3]) + 0.01*(roll[0]-rolls[0])
            if splay_ang < -15:
                splay_ang = -15
            elif splay_ang >15:
                splay_ang = 15    
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'R_first',[0,first_ang,splay_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'R_middle',[0,mid_ang,0])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'R_last',[0,last_ang,0])


## LITTLE FINGER
            first_ang = 0.01*(headings[4]-heading[4]) - 0.016*(pitchs[0]-pitch[0])
            if first_ang < -10:
                    first_ang = -10
            elif first_ang >150:
                first_ang = 150        
            mid_ang = 2*first_ang
            last_ang = 3*first_ang
            
            if mid_ang < 0:
                mid_ang = 0
            if last_ang < 0:
                last_ang = 0
            splay_ang = -0.01*(roll[4]-rolls[4]) + 0.01*(roll[0]-rolls[0])
            if splay_ang < -15:
                splay_ang = -15
            elif splay_ang >15:
                splay_ang = 15
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'L_first',[0,first_ang,splay_ang])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'L_middle',[0,mid_ang,0])
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'L_last',[0,last_ang,0])


# WRIST
#           first_ang = pitch[0]-pitchs[0]
            first_ang = 0.016*(pitchs[0]-pitch[0])
            if first_ang < -60:
                   first_ang = -60;
#           mid_ang = 2*first_ang
#            last_ang = 3*first_ang
#            splay_ang = 1.1*(headings[4]-heading[4])
            splay_ang = 0.01*(roll[0]-rolls[0])
            rot_ang = 0.016*(heading[0]-headings[0])
            if rot_ang < -150:
                rot_ang = -150
            elif rot_ang > 90: 
                rot_ang = 90 
            SetBoneRotationDeg(bpy.data.objects['Hand'], 'Wrist',[rot_ang,splay_ang,first_ang])

            
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP',iterations=1)
            
