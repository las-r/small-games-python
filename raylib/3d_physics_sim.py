from pyray import * #type:ignore
import math
import random

# 3d physics sim
# by las-r

# helpers
class Ball:
    def __init__(self, pos: Vector3, vel: Vector3, size, elas, col):
        self.pos = pos
        self.vel = vel
        self.r = size
        self.e = elas
        self.col = col
        
# settings
WIDTH, HEIGHT = 800, 600
FS = 20
HFS = FS / 2
grav = Vector3(0, -50, 0)
        
# init
init_window(WIDTH, HEIGHT, "3D Physics Simulation")
set_target_fps(60)
#disable_cursor()

# camera
cam = Camera3D()
cam.position = Vector3(0, FS / 1.5, FS * 2)
cam.target = Vector3(0, FS / 2, 0)
cam.up = Vector3(0, 1, 0)
cam.fovy = 45
cam.projection = CameraProjection.CAMERA_PERSPECTIVE
angle = 0.0
rotspeed = 0.2

# balls
balls = []

# main loop
paused = False
while not window_should_close():
    dt = get_frame_time()
    angle += rotspeed * dt
    cam.position.x = math.sin(angle) * (FS * 2)
    cam.position.z = math.cos(angle) * (FS * 2)
    update_camera(cam, CameraMode.CAMERA_CUSTOM)
    
    # input
    if is_key_pressed(KeyboardKey.KEY_R):
        balls = []
    if is_key_pressed(KeyboardKey.KEY_P):
        paused = not paused
    if is_key_down(KeyboardKey.KEY_SPACE):
        balls.append(
            Ball(
                Vector3(0, 20, 0),
                Vector3(random.uniform(-15, 15), random.uniform(-10, 10), random.uniform(-15, 15)),
                random.uniform(0.4, 2),
                random.uniform(0.1, 0.9),
                Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
            )
        )
    
    # physics
    if not paused:
        for b in balls:
            # update pos and vel
            b.pos = vector3_add(b.pos, vector3_scale(b.vel, dt))
            b.vel = vector3_add(b.vel, vector3_scale(grav, dt))
            
            # ball bounce
            for q in [q for q in balls if q != b]:
                d = vector3_distance(b.pos, q.pos)
                sr = b.r + q.r
                if d < sr:
                    # separate
                    n = vector3_normalize(vector3_subtract(q.pos, b.pos))
                    o = (sr - d) / 2
                    mvec = vector3_scale(n, o)
                    b.pos = vector3_subtract(b.pos, mvec)
                    q.pos = vector3_add(q.pos, mvec)
                    nv = vector3_dot_product(vector3_subtract(q.vel, b.vel), n)
                    if 0 > nv:
                        # impulse
                        e = min(b.e, q.e)
                        j = -(1 + e) * nv / 2
                        impulse = vector3_scale(n, j)
                        b.vel = vector3_subtract(b.vel, impulse)
                        q.vel = vector3_add(q.vel, impulse)
            
            # wall bounce
            if b.pos.x - b.r < -HFS:
                b.pos.x = -HFS + b.r
                b.vel.x = abs(b.vel.x * b.e)
            elif b.pos.x + b.r > HFS:
                b.pos.x = HFS - b.r
                b.vel.x = -abs(b.vel.x * b.e)
            if b.pos.y - b.r < 0:
                b.pos.y = b.r
                b.vel.y = abs(b.vel.y * b.e)
            elif b.pos.y + b.r > FS:
                b.pos.y = FS - b.r
                b.vel.y = -abs(b.vel.y * b.e)
            if b.pos.z - b.r < -HFS:
                b.pos.z = -HFS + b.r
                b.vel.z = abs(b.vel.z * b.e)
            elif b.pos.z + b.r > HFS:
                b.pos.z = HFS - b.r
                b.vel.z = -abs(b.vel.z * b.e)
    
    # draw
    begin_drawing()
    clear_background(BLACK)
    begin_mode_3d(cam)
    for b in balls:
        draw_sphere(b.pos, b.r, b.col)
    draw_grid(FS, 1)
    draw_cube_wires(Vector3(0, HFS, 0), FS, FS, FS, LIGHTGRAY)
    end_mode_3d()
    draw_text(f"Balls: {len(balls)}", 10, 10, 20, WHITE)
    draw_text(f"Paused: {paused}", 10, 30, 20, WHITE)
    draw_text(f"FPS: {get_fps()}", 10, 50, 20, WHITE)
    end_drawing()
    

# deinit
close_window()
