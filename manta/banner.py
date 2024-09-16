"""
This file contains the banner for the project.

The banner is a simple ASCII art. It uses block characters to create a simple manta logo.
ASCII color codes are used to color the banner.
There are color codes for the text and the background. This file contains the color codes for the text and background.
Text color codes are here 'CRED', 'CGREEN', ...
Background color codes are here 'CREDBG', 'CGREENBG', ...

The banner looks best when there is no additional spacing between row.
"""

END = '\33[0m'

CEND = '\33[0m'
CBOLD = '\33[1m'
CITALIC = '\33[3m'
CURL = '\33[4m'
CBLINK = '\33[5m'
CBLINK2 = '\33[6m'
CSELECTED = '\33[7m'

CBLACK = '\33[30m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE = '\33[36m'
CWHITE = '\33[37m'

CBLACKBG = '\33[40m'
CREDBG = '\33[41m'
CGREENBG = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG = '\33[46m'
CWHITEBG = '\33[47m'

CGREY = '\33[90m'
CRED2 = '\33[91m'
CGREEN2 = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2 = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2 = '\33[96m'
CWHITE2 = '\33[97m'

manta_sw = f"""
                ▄▄
              ▄▀ ▄▀                   ▄▄
              █  ▀▄▄                 █  ▀▄
              ▀▄   ▄▀▀▄▄            █    ▀▄
                █  █    ▀█▀▀▄▄  ▄▄▄▀      █
                ▄▀▀▀      █   ▀▀          █
   ▄▄         ▄▀                         █
  █  ▀▄▄▄▄▄▄▄▀                          ▄▀
  █   ▀▄                          ▄▄▄ ▄▀
   ▀▄   ▀▄                    ▄▄ ▀▀ ▄▀
     ▀▄   ▀▄          ▄▄    ▄ ▀▀   █
       ▀▀▄▄▄▀    ▄██▀ ▀▀  ▀▀  ▄▀▄  █
            ▀▀▀▀▀▀▀▀▄   ▄▀▀▀▀▀  ▀▄▀
                     ▀▄▄▄▀
                     
       ▟▙  ▂▟▛           ▟▛
      ▟▛▜▛▀█▛ ▟▛▀▙ ▟▛▀▙▝▟▛▘▘▟▛▀▙
     ▟▛   ▟▛ ▟▛▀▜▛▟▛ ▟▛ ▜▄ ▟▛▀▜▛
"""

P = CVIOLET
G = CGREY
W = CWHITE
banner_color = f"""{CGREY}
                ▄▄
              ▄▀ ▄▀                   ▄▄
              █  ▀▄▄                 █  ▀▄
              ▀▄   ▄▀▀▄▄            █    ▀▄
                █  █    ▀█▀▀▄▄  ▄▄▄▀      █
                ▄▀▀▀      █   ▀▀          █
   ▄▄         ▄▀                         █
  █  ▀▄▄▄▄▄▄▄▀                          ▄▀
  █   ▀▄                          {P}▄▄▄{G} ▄▀
   ▀▄   ▀▄                    {W}▄{G}▄ {P}▀▀▀{G}▄▀
     ▀▄   ▀▄          {W}▄{G}▄    ▄ ▀▀   █
       ▀▀▄▄▄▀    {P}▄██▀{G} ▀▀  ▀▀  ▄▀▄  █
            ▀▀▀▀▀▀▀▀▄   ▄▀▀▀▀▀  ▀▄▀
                     ▀▄▄▄▀{END}                           
                     
           ▟▙  ▂▟▛           ▟▛
          ▟▛▜▛▀█▛ ▟▛▀▙ ▟▛▀▙▝▟▛▘▘▟▛▀▙
         ▟▛   ▟▛ ▟▛▀▜▛▟▛ ▟▛ ▜▄ ▟▛▀▜▛
"""

b = CBEIGEBG
u = CVIOLETBG
e = f"{CEND}{CGREY}"
banner = f"""{CGREY}
                ▄▄
              ▄{b}▀ ▄{e}▀                   ▄▄
              █{b}  ▀{e}▄▄                 █{b}  ▀{e}▄
              ▀{b}▄   ▄▀▀{e}▄▄            █{b}    ▀{e}▄
                █{b}  █    ▀█▀▀{e}▄▄  ▄▄▄{b}▀      {e}█
                ▄{b}▀▀▀      █   ▀▀          {e}█
   ▄▄         ▄{b}▀                         {e}█
  █{u}  ▀{e}▄▄▄▄▄▄▄{b}▀                          ▄{e}▀
  █{u}   ▀{e}{b}▄                          {P}▄▄▄{G} ▄{e}▀
   ▀{u}▄   ▀{e}{b}▄                    {W}▄{G}▄ {P}▀▀▀{G}▄{e}▀
     ▀{u}▄   ▀{e}{b}▄          {W}▄{G}▄    ▄ ▀▀   {e}█
       ▀▀{u}▄▄▄{e}{b}▀    {P}▄██▀{G} ▀▀  ▀▀  ▄{e}▀{b}▄  {e}█
            ▀▀▀▀▀▀▀▀{b}▄   ▄{e}▀▀▀▀▀  ▀{b}▄{e}▀
                     ▀{b}▄▄▄{e}▀{END}                           

           ▟▙  ▂▟▛           ▟▛
          ▟▛▜▛▀█▛ ▟▛▀▙ ▟▛▀▙▝▟▛▘▘▟▛▀▙
         ▟▛   ▟▛ ▟▛▀▜▛▟▛ ▟▛ ▜▄ ▟▛▀▜▛
"""

if __name__ == '__main__':
    # print(banner)
    # print(banner_sw)
    print(banner)
