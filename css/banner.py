
from colored import attr, fg
from pystyle import Center, Colors, Colorate


#! Colored code
yellow = fg("yellow")
white = fg("white")
blue = fg(20)
blues = fg(27)
cyan = fg('cyan')
green = fg(46)
r124 = fg(124)
red = fg('red')
purple = fg("purple_1a")
grey = fg("grey_27")
org = fg('orange_red_1')
bold = attr("bold")
reset = attr("reset")


title = r'''
 ▀█▀ ██▀ █▄ ▄█ █▀▄ █▄ ▄█ ▄▀▄ █ █
  █  █▄▄ █ ▀ █ █▀  █ ▀ █ █▀█ █ █▄▄ ▄
'''
txt = r'BY: ══ᵂʰᵒᴬᴹ!'
bann = (Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(title), True))
text = (Colorate.Horizontal(Colors.black_to_white, Center.XCenter(txt), True))

logo = f'''
{bann}
    {text}
'''
strg = f' {"»" * 70} '

empty = f'  Your Mailbox is empty! '
checkinput = f'  Check your input! '
selectoption = f' Please select your option:  '
remtxt = f' Text file has been removed! '

generator = f'''
 [1]  Generate With Random Email 
 [2]  Generate With Custom Email 
 [3]  Check Inbox With Existing Email 
 [4]  Delete Email From Server 
 [5]  Exit Program 
'''

deletemail = f'''
 [1]  Delete Manually 
 [2]  Delete All in TXT File 
'''

custemail = f'''
 [1]  Random Username 
 [2]  Custom Username 
'''

custdom = f' Do you want to custom domain? Y|N '
