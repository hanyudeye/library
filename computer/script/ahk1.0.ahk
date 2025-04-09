CapsLock::Ctrl
!j:: Send {Down}
!k:: Send {Up}
!h:: Send {Left}
!l:: Send {Right}
!d::  ; Alt + D
Send, {Delete}  ; 模拟按下 Delete 键
return

;切换虚拟桌面
#^;::Send #^{Right}
#^j::Send #^{Left}

Active(t){
;     IfWinActive,%t%
;   {
;     WinMinimize
;     return
;   }

;    IfWinExist,%t%
;   {
;     WinShow
;     WinActivate           
;     return 1
;   }
 WinActivate,ahk_exe %t%
 return
}

Match(){
SetTitleMatchMode, 2
; 使用正则表达式匹配窗口标题并激活
RegexPattern := "WinActivate.*"
 
; 检查是否存在匹配窗口标题的窗口
;ahk_class Chrome_WidgetWin_1 ahk_exe msedge.exe 
if WinExist( RegexPattern)
{
    ; 如果存在，则激活窗口
    WinActivate
MsgBox hello
}

return
 }

;切换窗口
ToggleQuakeWindowT(windowT)
{
    ; 查找窗口
    WinGet, windowID, ID,  %windowT%
    ; 如果窗口存在，则隐藏/显示
    if (windowID)
    {

        WinGet, windowState, MinMax, ahk_id %windowID%
        if (windowState)
	{
            WinRestore ahk_id %windowID%
            WinWait,%windowT%
            WinActivate
	}
        else
            WinMinimize ahk_id %windowID%
    }

}


;激活资源管理器
#e::ToggleQuakeWindowT("ahk_class CabinetWClass")
;#e::Active("Explorer.EXE")
;#a::WinActivate, EasyChat
;#w::Active("msedge.exe")
#a::
#w::ToggleQuakeWindowT("ahk_exe msedge.exe")

f1::ToggleQuakeWindowT("ahk_exe Code.exe")
#c::ToggleQuakeWindowT("ahk_exe Cursor.exe")
#i::ToggleQuakeWindowT("ahk_exe WindowsTerminal.exe")
#o::ToggleQuakeWindowT("ahk_exe okular.exe")
#s::ToggleQuakeWindowT("ahk_exe chrome.exe")
;#s::Active("chrome.exe")
#y::Active("copytranslator.exe")
;#a::ToggleQuakeWindowT("ahk_exe Postman.exe")
#x::WinActivate,Telegram

;激活Code Shijian
#+s::
WinTitle=ahk_class Chrome_WidgetWin_1
main:
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"Shijian")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return


;激活Code Lilun
#+l::
WinTitle=ahk_class Chrome_WidgetWin_1
WinGet, winList,List,%WinTitle%
wins:=[]
Loop,%winList%
{
    this_id=% winList%A_Index%
    WinGetTitle,this_title,ahk_id %this_id%
    wins.Insert({index:A_Index,title:this_title,id:this_id})
    ;MsgBox  %this_id%
}

main_flag:=box_flag:=message_flag:=0
for each,win in wins
{

   if InStr(win.title,"blog")
		{
			main_id:=win.id
			WinActivate,ahk_id %main_id%
			
		}
}

return
