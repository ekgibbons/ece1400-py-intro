import io
import contextlib
import random
import subprocess
import unittest

import numpy as np

import intro_sol
import sphere

class TestIntro(unittest.TestCase):

    def test_hello(self):

        print("\ntesting hello_world.py")
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            intro_sol.hello_world()
        hello_string_sol = f.getvalue().strip()

        result = subprocess.run(["python","hello_world.py"],
                                stdout=subprocess.PIPE)
        hello_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(hello_string_sol, hello_string)

    def test_wheel(self):

        print("\ntesting wheel.py")

        with open("wheel.py", "r") as file:
            content = file.read()

        hard_code_check = False
        # check if string present or not
        if "190.44" in content:
            hard_code_check = True

        self.assertFalse(hard_code_check,
                         "You are illegally hard "
                         "coding the answer")

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            intro_sol.wheel()
        wheel_string_sol = f.getvalue().strip()

        result = subprocess.run(["python","wheel.py"],
                                stdout=subprocess.PIPE)
        wheel_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(wheel_string_sol, wheel_string)


    def test_flux(self):

        print("\ntesting flux.py")

        with open("flux.py", "r") as file:
            content = file.read()

        hard_code_check = False
        # check if string present or not
        if "0.0032031" in content:
            hard_code_check = True

        self.assertFalse(hard_code_check,
                         "You are illegally hard "
                         "coding the answer")


        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            intro_sol.flux()
        flux_string_sol = f.getvalue().strip()

        result = subprocess.run(["python","flux.py"],
                                stdout=subprocess.PIPE)
        flux_string = result.stdout.decode("UTF-8").strip()

        if "1351258" in flux_string:
            print("---fixing rounding issue---")
            flux_string = flux_string.replace("1351258","13512576")
        
        self.assertEqual(flux_string_sol, flux_string)


    def test_sphere_volume(self):

        print("\ntesting sphere.sphere_volume()")

        radius = 10*random.random()
        sol = intro_sol.sphere_volume(radius)
        sub = sphere.sphere_volume(radius)

        self.assertEqual(sol, sub)


    def test_sphere_area(self):

        print("\ntesting sphere.sphere_area()")

        radius = 10*random.random()
        sol = intro_sol.sphere_area(radius)
        sub = sphere.sphere_area(radius)

        self.assertEqual(sol, sub)

    def test_sphere_script(self):

        print("\ntesting sphere script.py")

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            intro_sol.sphere_script()
        sphere_string_sol = f.getvalue().strip()

        
        result = subprocess.run(["python","sphere.py"],
                                stdout=subprocess.PIPE)
        sphere_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(sphere_string_sol, sphere_string)
        

if __name__ == '__main__':
    unittest.main()




