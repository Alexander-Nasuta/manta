from examples.kioptipack.open_hub_day_datenfluss2 import OpenHubDaysDatenflussOnto
from examples.kioptipack.openhub_day_agenda1 import OpenHubDaysAgenda1
from examples.kioptipack.openhub_day_agenda2 import OpenHubDaysAgenda2
from examples.kioptipack.openhub_day_intro import OpenHubDayIntro


import subprocess

from examples.kioptipack.openhub_day_ml import OpenHubDaysMLSlides

if __name__ == '__main__':

    if False:
        OpenHubDayIntro.manim_slides_m()
        OpenHubDaysAgenda1.manim_slides_m()
        OpenHubDaysDatenfluss.manim_slides_m()
        #OpenHubDaysAgenda2.manim_slides_m()
        #OpenHubDaysMLSlides.manim_slides_m()
        #OpenHubDaysDatenfluss.manim_slides_m()

        # wait 5 seconds
        import time
        time.sleep(5)
        # exit program
        exit()



    # run manim slides
    terminal_cmd = f"manim-slides convert OpenHubDayIntro OpenHubDaysAgenda1 slides-complete2.html --open"
    print(f"running command: \n\n\t{terminal_cmd}\n")
    try:
        result = subprocess.run(terminal_cmd, shell=True, check=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(e.stderr.decode())
        raise e