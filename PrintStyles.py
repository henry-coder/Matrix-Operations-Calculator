class PrintStyles:
    '''
    PrintStyles class to implement styles in terminal outputs in a simpler way
    '''
    # formats
    RESET     = '\033[0m'
    BOLD      = '\033[1m'
    ITALIC    = '\033[3m'
    UNDERLINE = '\033[4m'
    SELECTED  = '\033[7m'
    # colors
    BLACK  = '\033[30m'
    RED    = '\033[31m'
    GREEN  = '\033[32m'
    YELLOW = '\033[33m'
    BLUE   = '\033[34m'
    VIOLET = '\033[35m'
    CYAN   = '\033[36m'
    WHITE  = '\033[37m'
    GREY   = '\033[90m'
    # backgrounds
    BLACKBG  = '\033[40m'
    REDBG    = '\033[41m'
    GREENBG  = '\033[42m'
    YELLOWBG = '\033[43m'
    BLUEBG   = '\033[44m'
    VIOLETBG = '\033[45m'
    CYANBG   = '\033[46m'
    WHITEBG  = '\033[47m'
    GREYBG   = '\033[100m'

    # formats+colors
    # BOLD+color
    BBLACK  = '\033[1;30m'
    BRED    = '\033[1;31m'
    BGREEN  = '\033[1;32m'
    BYELLOW = '\033[1;33m'
    BBLUE   = '\033[1;34m'
    BVIOLET = '\033[1;35m'
    BCYAN   = '\033[1;36m'
    BWHITE  = '\033[1;37m'
    BGREY   = '\033[1;90m'
    # ITALIC+color
    IBLACK  = '\033[3;30m'
    IRED    = '\033[3;31m'
    IGREEN  = '\033[3;32m'
    IYELLOW = '\033[3;33m'
    IBLUE   = '\033[3;34m'
    IVIOLET = '\033[3;35m'
    ICYAN   = '\033[3;36m'
    IWHITE  = '\033[3;37m'
    IGREY   = '\033[3;90m'
    # UNDERLINE+color
    UBLACK  = '\033[4;30m'
    URED    = '\033[4;31m'
    UGREEN  = '\033[4;32m'
    UYELLOW = '\033[4;33m'
    UBLUE   = '\033[4;34m'
    UVIOLET = '\033[4;35m'
    UCYAN   = '\033[4;36m'
    UWHITE  = '\033[4;37m'
    UGREY   = '\033[4;90m'
    # SELECT+color
    SBLACK  = '\033[7;30m'
    SRED    = '\033[7;31m'
    SGREEN  = '\033[7;32m'
    SYELLOW = '\033[7;33m'
    SBLUE   = '\033[7;34m'
    SVIOLET = '\033[7;35m'
    SCYAN   = '\033[7;36m'
    SWHITE  = '\033[7;37m'
    SGREY   = '\033[7;90m'

    # formats+backgrounds
    # BOLD+background
    BBLACKBG  = '\033[1;40m'
    BREDBG    = '\033[1;41m'
    BGREENBG  = '\033[1;42m'
    BYELLOWBG = '\033[1;43m'
    BBLUEBG   = '\033[1;44m'
    BVIOLETBG = '\033[1;45m'
    BCYANBG   = '\033[1;46m'
    BWHITEBG  = '\033[1;47m'
    BGREYBG   = '\033[1;100m'
    # ITALIC+background
    IBLACKBG  = '\033[3;40m'
    IREDBG    = '\033[3;41m'
    IGREENBG  = '\033[3;42m'
    IYELLOWBG = '\033[3;43m'
    IBLUEBG   = '\033[3;44m'
    IVIOLETBG = '\033[3;45m'
    ICYANBG   = '\033[3;46m'
    IWHITEBG  = '\033[3;47m'
    IGREYBG   = '\033[3;100m'
    # UNDERLINE+background
    UBLACKBG  = '\033[4;40m'
    UREDBG    = '\033[4;41m'
    UGREENBG  = '\033[4;42m'
    UYELLOWBG = '\033[4;43m'
    UBLUEBG   = '\033[4;44m'
    UVIOLETBG = '\033[4;45m'
    UCYANBG   = '\033[4;46m'
    UWHITEBG  = '\033[4;47m'
    UGREYBG   = '\033[4;100m'
    #SELECT+background
    SBLACKBG  = '\033[7;40m'
    SREDBG    = '\033[7;41m'
    SGREENBG  = '\033[7;42m'
    SYELLOWBG = '\033[7;43m'
    SBLUEBG   = '\033[7;44m'
    SVIOLETBG = '\033[7;45m'
    SCYANBG   = '\033[7;46m'
    SWHITEBG  = '\033[7;47m'
    SGREYBG   = '\033[7;100m'

    # colors+backgrounds
    # BLACK+background
    BLACK_BLACKBG  = '\033[30;40m'
    BLACK_REDBG    = '\033[30;41m'
    BLACK_GREENBG  = '\033[30;42m'
    BLACK_YELLOWBG = '\033[30;43m'
    BLACK_BLUEBG   = '\033[30;44m'
    BLACK_VIOLETBG = '\033[30;45m'
    BLACK_CYANBG   = '\033[30;46m'
    BLACK_WHITEBG  = '\033[30;47m'
    BLACK_GREYBG   = '\033[30;100m'
    # RED+background
    RED_BLACKBG  = '\033[31;40m'
    RED_REDBG    = '\033[31;41m'
    RED_GREENBG  = '\033[31;42m'
    RED_YELLOWBG = '\033[31;43m'
    RED_BLUEBG   = '\033[31;44m'
    RED_VIOLETBG = '\033[31;45m'
    RED_CYANBG   = '\033[31;46m'
    RED_WHITEBG  = '\033[31;47m'
    RED_GREYBG   = '\033[31;100m'
    # GREEN+background
    GREEN_BLACKBG  = '\033[32;40m'
    GREEN_REDBG    = '\033[32;41m'
    GREEN_GREENBG  = '\033[32;42m'
    GREEN_YELLOWBG = '\033[32;43m'
    GREEN_BLUEBG   = '\033[32;44m'
    GREEN_VIOLETBG = '\033[32;45m'
    GREEN_CYANBG   = '\033[32;46m'
    GREEN_WHITEBG  = '\033[32;47m'
    GREEN_GREYBG   = '\033[32;100m'
    # YELLOW+background
    YELLOW_BLACKBG  = '\033[33;40m'
    YELLOW_REDBG    = '\033[33;41m'
    YELLOW_GREENBG  = '\033[33;42m'
    YELLOW_YELLOWBG = '\033[33;43m'
    YELLOW_BLUEBG   = '\033[33;44m'
    YELLOW_VIOLETBG = '\033[33;45m'
    YELLOW_CYANBG   = '\033[33;46m'
    YELLOW_WHITEBG  = '\033[33;47m'
    YELLOW_GREYBG   = '\033[33;100m'
    # BLUE+background
    BLUE_BLACKBG  = '\033[34;40m'
    BLUE_REDBG    = '\033[34;41m'
    BLUE_GREENBG  = '\033[34;42m'
    BLUE_YELLOWBG = '\033[34;43m'
    BLUE_BLUEBG   = '\033[34;44m'
    BLUE_VIOLETBG = '\033[34;45m'
    BLUE_CYANBG   = '\033[34;46m'
    BLUE_WHITEBG  = '\033[34;47m'
    BLUE_GREYBG   = '\033[34;100m'
    # VIOLET+background
    VIOLET_BLACKBG  = '\033[35;40m'
    VIOLET_REDBG    = '\033[35;41m'
    VIOLET_GREENBG  = '\033[35;42m'
    VIOLET_YELLOWBG = '\033[35;43m'
    VIOLET_BLUEBG   = '\033[35;44m'
    VIOLET_VIOLETBG = '\033[35;45m'
    VIOLET_CYANBG   = '\033[35;46m'
    VIOLET_WHITEBG  = '\033[35;47m'
    VIOLET_GREYBG   = '\033[35;100m'
    # CYAN+background
    CYAN_BLACKBG  = '\033[36;40m'
    CYAN_REDBG    = '\033[36;41m'
    CYAN_GREENBG  = '\033[36;42m'
    CYAN_YELLOWBG = '\033[36;43m'
    CYAN_BLUEBG   = '\033[36;44m'
    CYAN_VIOLETBG = '\033[36;45m'
    CYAN_CYANBG   = '\033[36;46m'
    CYAN_WHITEBG  = '\033[36;47m'
    CYAN_GREYBG   = '\033[36;100m'
    # WHITE+background
    WHITE_BLACKBG  = '\033[37;40m'
    WHITE_REDBG    = '\033[37;41m'
    WHITE_GREENBG  = '\033[37;42m'
    WHITE_YELLOWBG = '\033[37;43m'
    WHITE_BLUEBG   = '\033[37;44m'
    WHITE_VIOLETBG = '\033[37;45m'
    WHITE_CYANBG   = '\033[37;46m'
    WHITE_WHITEBG  = '\033[37;47m'
    WHITE_GREYBG   = '\033[37;100m'    
    # GREY+background
    GREY_BLACKBG  = '\033[90;40m'
    GREY_REDBG    = '\033[90;41m'
    GREY_GREENBG  = '\033[90;42m'
    GREY_YELLOWBG = '\033[90;43m'
    GREY_BLUEBG   = '\033[90;44m'
    GREY_VIOLETBG = '\033[90;45m'
    GREY_CYANBG   = '\033[90;46m'
    GREY_WHITEBG  = '\033[90;47m'
    GREY_GREYBG   = '\033[90;100m'

    # formats+colors+backgrounds
    # BOLD+colors+background        
    # BOLD+BLACK+background
    BBLACK_BLACKBG = '\033[1;30;40m' 
    BBLACK_REDBG = '\033[1;30;41m'   
    BBLACK_GREENBG = '\033[1;30;42m' 
    BBLACK_YELLOWBG = '\033[1;30;43m'
    BBLACK_BLUEBG = '\033[1;30;44m'  
    BBLACK_VIOLETBG = '\033[1;30;45m'
    BBLACK_CYANBG = '\033[1;30;46m'  
    BBLACK_WHITEBG = '\033[1;30;47m' 
    BBLACK_GREYBG = '\033[1;30;100m' 
    # BOLD+RED+background
    BRED_BLACKBG = '\033[1;31;40m'   
    BRED_REDBG = '\033[1;31;41m'     
    BRED_GREENBG = '\033[1;31;42m'   
    BRED_YELLOWBG = '\033[1;31;43m'  
    BRED_BLUEBG = '\033[1;31;44m'    
    BRED_VIOLETBG = '\033[1;31;45m'  
    BRED_CYANBG = '\033[1;31;46m'    
    BRED_WHITEBG = '\033[1;31;47m'   
    BRED_GREYBG = '\033[1;31;100m'   
    # BOLD+GREEN+background
    BGREEN_BLACKBG = '\033[1;32;40m' 
    BGREEN_REDBG = '\033[1;32;41m'   
    BGREEN_GREENBG = '\033[1;32;42m' 
    BGREEN_YELLOWBG = '\033[1;32;43m'
    BGREEN_BLUEBG = '\033[1;32;44m'  
    BGREEN_VIOLETBG = '\033[1;32;45m'
    BGREEN_CYANBG = '\033[1;32;46m'  
    BGREEN_WHITEBG = '\033[1;32;47m' 
    BGREEN_GREYBG = '\033[1;32;100m' 
    # BOLD+YELLOW+background
    BYELLOW_BLACKBG = '\033[1;33;40m'
    BYELLOW_REDBG = '\033[1;33;41m'
    BYELLOW_GREENBG = '\033[1;33;42m'
    BYELLOW_YELLOWBG = '\033[1;33;43m'
    BYELLOW_BLUEBG = '\033[1;33;44m'
    BYELLOW_VIOLETBG = '\033[1;33;45m'
    BYELLOW_CYANBG = '\033[1;33;46m'
    BYELLOW_WHITEBG = '\033[1;33;47m'
    BYELLOW_GREYBG = '\033[1;33;100m'
    # BOLD+BLUE+background
    BBLUE_BLACKBG = '\033[1;34;40m'
    BBLUE_REDBG = '\033[1;34;41m'
    BBLUE_GREENBG = '\033[1;34;42m'
    BBLUE_YELLOWBG = '\033[1;34;43m'
    BBLUE_BLUEBG = '\033[1;34;44m'
    BBLUE_VIOLETBG = '\033[1;34;45m'
    BBLUE_CYANBG = '\033[1;34;46m'
    BBLUE_WHITEBG = '\033[1;34;47m'
    BBLUE_GREYBG = '\033[1;34;100m'
    # BOLD+VIOLET+background
    BVIOLET_BLACKBG = '\033[1;35;40m'
    BVIOLET_REDBG = '\033[1;35;41m'
    BVIOLET_GREENBG = '\033[1;35;42m'
    BVIOLET_YELLOWBG = '\033[1;35;43m'
    BVIOLET_BLUEBG = '\033[1;35;44m'
    BVIOLET_VIOLETBG = '\033[1;35;45m'
    BVIOLET_CYANBG = '\033[1;35;46m'
    BVIOLET_WHITEBG = '\033[1;35;47m'
    BVIOLET_GREYBG = '\033[1;35;100m'
    # BOLD+CYAN+background
    BCYAN_BLACKBG = '\033[1;36;40m'
    BCYAN_REDBG = '\033[1;36;41m'
    BCYAN_GREENBG = '\033[1;36;42m'
    BCYAN_YELLOWBG = '\033[1;36;43m'
    BCYAN_BLUEBG = '\033[1;36;44m'
    BCYAN_VIOLETBG = '\033[1;36;45m'
    BCYAN_CYANBG = '\033[1;36;46m'
    BCYAN_WHITEBG = '\033[1;36;47m'
    BCYAN_GREYBG = '\033[1;36;100m'
    # BOLD+WHITE+background
    BWHITE_BLACKBG = '\033[1;37;40m'
    BWHITE_REDBG = '\033[1;37;41m'
    BWHITE_GREENBG = '\033[1;37;42m'
    BWHITE_YELLOWBG = '\033[1;37;43m'
    BWHITE_BLUEBG = '\033[1;37;44m'
    BWHITE_VIOLETBG = '\033[1;37;45m'
    BWHITE_CYANBG = '\033[1;37;46m'
    BWHITE_WHITEBG = '\033[1;37;47m'
    BWHITE_GREYBG = '\033[1;37;100m'
    # BOLD+GREY+background
    BGREY_BLACKBG = '\033[1;90;40m'
    BGREY_REDBG = '\033[1;90;41m'
    BGREY_GREENBG = '\033[1;90;42m'
    BGREY_YELLOWBG = '\033[1;90;43m'
    BGREY_BLUEBG = '\033[1;90;44m'
    BGREY_VIOLETBG = '\033[1;90;45m'
    BGREY_CYANBG = '\033[1;90;46m'
    BGREY_WHITEBG = '\033[1;90;47m'
    BGREY_GREYBG = '\033[1;90;100m'

    # ITALIC+colors+background
    # ITALIC+BLACK+background
    IBLACK_BLACKBG = '\033[3;30;40m'
    IBLACK_REDBG = '\033[3;30;41m'
    IBLACK_GREENBG = '\033[3;30;42m'
    IBLACK_YELLOWBG = '\033[3;30;43m'
    IBLACK_BLUEBG = '\033[3;30;44m'
    IBLACK_VIOLETBG = '\033[3;30;45m'
    IBLACK_CYANBG = '\033[3;30;46m'
    IBLACK_WHITEBG = '\033[3;30;47m'
    IBLACK_GREYBG = '\033[3;30;100m'
    # ITALIC+RED+background
    IRED_BLACKBG = '\033[3;31;40m'
    IRED_REDBG = '\033[3;31;41m'
    IRED_GREENBG = '\033[3;31;42m'
    IRED_YELLOWBG = '\033[3;31;43m'
    IRED_BLUEBG = '\033[3;31;44m'
    IRED_VIOLETBG = '\033[3;31;45m'
    IRED_CYANBG = '\033[3;31;46m'
    IRED_WHITEBG = '\033[3;31;47m'
    IRED_GREYBG = '\033[3;31;100m'
    # ITALIC+GREEN+background
    IGREEN_BLACKBG = '\033[3;32;40m'
    IGREEN_REDBG = '\033[3;32;41m'
    IGREEN_GREENBG = '\033[3;32;42m'
    IGREEN_YELLOWBG = '\033[3;32;43m'
    IGREEN_BLUEBG = '\033[3;32;44m'
    IGREEN_VIOLETBG = '\033[3;32;45m'
    IGREEN_CYANBG = '\033[3;32;46m'
    IGREEN_WHITEBG = '\033[3;32;47m'
    IGREEN_GREYBG = '\033[3;32;100m'
    # ITALIC+YELLOW+background
    IYELLOW_BLACKBG = '\033[3;33;40m'
    IYELLOW_REDBG = '\033[3;33;41m'
    IYELLOW_GREENBG = '\033[3;33;42m'
    IYELLOW_YELLOWBG = '\033[3;33;43m'
    IYELLOW_BLUEBG = '\033[3;33;44m'
    IYELLOW_VIOLETBG = '\033[3;33;45m'
    IYELLOW_CYANBG = '\033[3;33;46m'
    IYELLOW_WHITEBG = '\033[3;33;47m'
    IYELLOW_GREYBG = '\033[3;33;100m'
    # ITALIC+BLUE+background
    IBLUE_BLACKBG = '\033[3;34;40m'
    IBLUE_REDBG = '\033[3;34;41m'
    IBLUE_GREENBG = '\033[3;34;42m'
    IBLUE_YELLOWBG = '\033[3;34;43m'
    IBLUE_BLUEBG = '\033[3;34;44m'
    IBLUE_VIOLETBG = '\033[3;34;45m'
    IBLUE_CYANBG = '\033[3;34;46m'
    IBLUE_WHITEBG = '\033[3;34;47m'
    IBLUE_GREYBG = '\033[3;34;100m'
    # ITALIC+VIOLET+background
    IVIOLET_BLACKBG = '\033[3;35;40m'
    IVIOLET_REDBG = '\033[3;35;41m'
    IVIOLET_GREENBG = '\033[3;35;42m'
    IVIOLET_YELLOWBG = '\033[3;35;43m'
    IVIOLET_BLUEBG = '\033[3;35;44m'
    IVIOLET_VIOLETBG = '\033[3;35;45m'
    IVIOLET_CYANBG = '\033[3;35;46m'
    IVIOLET_WHITEBG = '\033[3;35;47m'
    IVIOLET_GREYBG = '\033[3;35;100m'
    # ITALIC+CYAN+background
    ICYAN_BLACKBG = '\033[3;36;40m'
    ICYAN_REDBG = '\033[3;36;41m'
    ICYAN_GREENBG = '\033[3;36;42m'
    ICYAN_YELLOWBG = '\033[3;36;43m'
    ICYAN_BLUEBG = '\033[3;36;44m'
    ICYAN_VIOLETBG = '\033[3;36;45m'
    ICYAN_CYANBG = '\033[3;36;46m'
    ICYAN_WHITEBG = '\033[3;36;47m'
    ICYAN_GREYBG = '\033[3;36;100m'
    # ITALIC+WHITE+background
    IWHITE_BLACKBG = '\033[3;37;40m'
    IWHITE_REDBG = '\033[3;37;41m'
    IWHITE_GREENBG = '\033[3;37;42m'
    IWHITE_YELLOWBG = '\033[3;37;43m'
    IWHITE_BLUEBG = '\033[3;37;44m'
    IWHITE_VIOLETBG = '\033[3;37;45m'
    IWHITE_CYANBG = '\033[3;37;46m'
    IWHITE_WHITEBG = '\033[3;37;47m'
    IWHITE_GREYBG = '\033[3;37;100m'
    # ITALIC+GREY+background
    IGREY_BLACKBG = '\033[3;90;40m'
    IGREY_REDBG = '\033[3;90;41m'
    IGREY_GREENBG = '\033[3;90;42m'
    IGREY_YELLOWBG = '\033[3;90;43m'
    IGREY_BLUEBG = '\033[3;90;44m'
    IGREY_VIOLETBG = '\033[3;90;45m'
    IGREY_CYANBG = '\033[3;90;46m'
    IGREY_WHITEBG = '\033[3;90;47m'
    IGREY_GREYBG = '\033[3;90;100m'

    # UNDERLINE+colors+background
    # UNDERLINE+BLACK+background
    UBLACK_BLACKBG = '\033[4;30;40m'
    UBLACK_REDBG = '\033[4;30;41m'
    UBLACK_GREENBG = '\033[4;30;42m'
    UBLACK_YELLOWBG = '\033[4;30;43m'
    UBLACK_BLUEBG = '\033[4;30;44m'
    UBLACK_VIOLETBG = '\033[4;30;45m'
    UBLACK_CYANBG = '\033[4;30;46m'
    UBLACK_WHITEBG = '\033[4;30;47m'
    UBLACK_GREYBG = '\033[4;30;100m'
    # UNDERLINE+RED+background
    URED_BLACKBG = '\033[4;31;40m'
    URED_REDBG = '\033[4;31;41m'
    URED_GREENBG = '\033[4;31;42m'
    URED_YELLOWBG = '\033[4;31;43m'
    URED_BLUEBG = '\033[4;31;44m'
    URED_VIOLETBG = '\033[4;31;45m'
    URED_CYANBG = '\033[4;31;46m'
    URED_WHITEBG = '\033[4;31;47m'
    URED_GREYBG = '\033[4;31;100m'
    # UNDERLINE+GREEN+background
    UGREEN_BLACKBG = '\033[4;32;40m'
    UGREEN_REDBG = '\033[4;32;41m'
    UGREEN_GREENBG = '\033[4;32;42m'
    UGREEN_YELLOWBG = '\033[4;32;43m'
    UGREEN_BLUEBG = '\033[4;32;44m'
    UGREEN_VIOLETBG = '\033[4;32;45m'
    UGREEN_CYANBG = '\033[4;32;46m'
    UGREEN_WHITEBG = '\033[4;32;47m'
    UGREEN_GREYBG = '\033[4;32;100m'
    # UNDERLINE+YELLOW+background
    UYELLOW_BLACKBG = '\033[4;33;40m'
    UYELLOW_REDBG = '\033[4;33;41m'
    UYELLOW_GREENBG = '\033[4;33;42m'
    UYELLOW_YELLOWBG = '\033[4;33;43m'
    UYELLOW_BLUEBG = '\033[4;33;44m'
    UYELLOW_VIOLETBG = '\033[4;33;45m'
    UYELLOW_CYANBG = '\033[4;33;46m'
    UYELLOW_WHITEBG = '\033[4;33;47m'
    UYELLOW_GREYBG = '\033[4;33;100m'
    # UNDERLINE+BLUE+background
    UBLUE_BLACKBG = '\033[4;34;40m'
    UBLUE_REDBG = '\033[4;34;41m'
    UBLUE_GREENBG = '\033[4;34;42m'
    UBLUE_YELLOWBG = '\033[4;34;43m'
    UBLUE_BLUEBG = '\033[4;34;44m'
    UBLUE_VIOLETBG = '\033[4;34;45m'
    UBLUE_CYANBG = '\033[4;34;46m'
    UBLUE_WHITEBG = '\033[4;34;47m'
    UBLUE_GREYBG = '\033[4;34;100m'
    # UNDERLINE+VIOLET+background
    UVIOLET_BLACKBG = '\033[4;35;40m'
    UVIOLET_REDBG = '\033[4;35;41m'
    UVIOLET_GREENBG = '\033[4;35;42m'
    UVIOLET_YELLOWBG = '\033[4;35;43m'
    UVIOLET_BLUEBG = '\033[4;35;44m'
    UVIOLET_VIOLETBG = '\033[4;35;45m'
    UVIOLET_CYANBG = '\033[4;35;46m'
    UVIOLET_WHITEBG = '\033[4;35;47m'
    UVIOLET_GREYBG = '\033[4;35;100m'
    # UNDERLINE+CYAN+background
    UCYAN_BLACKBG = '\033[4;36;40m'
    UCYAN_REDBG = '\033[4;36;41m'
    UCYAN_GREENBG = '\033[4;36;42m'
    UCYAN_YELLOWBG = '\033[4;36;43m'
    UCYAN_BLUEBG = '\033[4;36;44m'
    UCYAN_VIOLETBG = '\033[4;36;45m'
    UCYAN_CYANBG = '\033[4;36;46m'
    UCYAN_WHITEBG = '\033[4;36;47m'
    UCYAN_GREYBG = '\033[4;36;100m'
    # UNDERLINE+WHITE+background
    UWHITE_BLACKBG = '\033[4;37;40m'
    UWHITE_REDBG = '\033[4;37;41m'
    UWHITE_GREENBG = '\033[4;37;42m'
    UWHITE_YELLOWBG = '\033[4;37;43m'
    UWHITE_BLUEBG = '\033[4;37;44m'
    UWHITE_VIOLETBG = '\033[4;37;45m'
    UWHITE_CYANBG = '\033[4;37;46m'
    UWHITE_WHITEBG = '\033[4;37;47m'
    UWHITE_GREYBG = '\033[4;37;100m'
    # UNDERLINE+GREY+background
    UGREY_BLACKBG = '\033[4;90;40m'
    UGREY_REDBG = '\033[4;90;41m'
    UGREY_GREENBG = '\033[4;90;42m'
    UGREY_YELLOWBG = '\033[4;90;43m'
    UGREY_BLUEBG = '\033[4;90;44m'
    UGREY_VIOLETBG = '\033[4;90;45m'
    UGREY_CYANBG = '\033[4;90;46m'
    UGREY_WHITEBG = '\033[4;90;47m'
    UGREY_GREYBG = '\033[4;90;100m'

    # SELECTED+colors+background
    # SELECTED+BLACK+background
    SBLACK_BLACKBG = '\033[7;30;40m'
    SBLACK_REDBG = '\033[7;30;41m'
    SBLACK_GREENBG = '\033[7;30;42m'
    SBLACK_YELLOWBG = '\033[7;30;43m'
    SBLACK_BLUEBG = '\033[7;30;44m'
    SBLACK_VIOLETBG = '\033[7;30;45m'
    SBLACK_CYANBG = '\033[7;30;46m'
    SBLACK_WHITEBG = '\033[7;30;47m'
    SBLACK_GREYBG = '\033[7;30;100m'
    # SELECTED+RED+background
    SRED_BLACKBG = '\033[7;31;40m'
    SRED_REDBG = '\033[7;31;41m'
    SRED_GREENBG = '\033[7;31;42m'
    SRED_YELLOWBG = '\033[7;31;43m'
    SRED_BLUEBG = '\033[7;31;44m'
    SRED_VIOLETBG = '\033[7;31;45m'
    SRED_CYANBG = '\033[7;31;46m'
    SRED_WHITEBG = '\033[7;31;47m'
    SRED_GREYBG = '\033[7;31;100m'
    # SELECTED+GREEN+background
    SGREEN_BLACKBG = '\033[7;32;40m'
    SGREEN_REDBG = '\033[7;32;41m'
    SGREEN_GREENBG = '\033[7;32;42m'
    SGREEN_YELLOWBG = '\033[7;32;43m'
    SGREEN_BLUEBG = '\033[7;32;44m'
    SGREEN_VIOLETBG = '\033[7;32;45m'
    SGREEN_CYANBG = '\033[7;32;46m'
    SGREEN_WHITEBG = '\033[7;32;47m'
    SGREEN_GREYBG = '\033[7;32;100m'
    # SELECTED+YELLOW+background
    SYELLOW_BLACKBG = '\033[7;33;40m'
    SYELLOW_REDBG = '\033[7;33;41m'
    SYELLOW_GREENBG = '\033[7;33;42m'
    SYELLOW_YELLOWBG = '\033[7;33;43m'
    SYELLOW_BLUEBG = '\033[7;33;44m'
    SYELLOW_VIOLETBG = '\033[7;33;45m'
    SYELLOW_CYANBG = '\033[7;33;46m'
    SYELLOW_WHITEBG = '\033[7;33;47m'
    SYELLOW_GREYBG = '\033[7;33;100m'
    # SELECTED+BLUE+background
    SBLUE_BLACKBG = '\033[7;34;40m'
    SBLUE_REDBG = '\033[7;34;41m'
    SBLUE_GREENBG = '\033[7;34;42m'
    SBLUE_YELLOWBG = '\033[7;34;43m'
    SBLUE_BLUEBG = '\033[7;34;44m'
    SBLUE_VIOLETBG = '\033[7;34;45m'
    SBLUE_CYANBG = '\033[7;34;46m'
    SBLUE_WHITEBG = '\033[7;34;47m'
    SBLUE_GREYBG = '\033[7;34;100m'
    # SELECTED+VIOLET+background
    SVIOLET_BLACKBG = '\033[7;35;40m'
    SVIOLET_REDBG = '\033[7;35;41m'
    SVIOLET_GREENBG = '\033[7;35;42m'
    SVIOLET_YELLOWBG = '\033[7;35;43m'
    SVIOLET_BLUEBG = '\033[7;35;44m'
    SVIOLET_VIOLETBG = '\033[7;35;45m'
    SVIOLET_CYANBG = '\033[7;35;46m'
    SVIOLET_WHITEBG = '\033[7;35;47m'
    SVIOLET_GREYBG = '\033[7;35;100m'
    # SELECTED+CYAN+background
    SCYAN_BLACKBG = '\033[7;36;40m'
    SCYAN_REDBG = '\033[7;36;41m'
    SCYAN_GREENBG = '\033[7;36;42m'
    SCYAN_YELLOWBG = '\033[7;36;43m'
    SCYAN_BLUEBG = '\033[7;36;44m'
    SCYAN_VIOLETBG = '\033[7;36;45m'
    SCYAN_CYANBG = '\033[7;36;46m'
    SCYAN_WHITEBG = '\033[7;36;47m'
    SCYAN_GREYBG = '\033[7;36;100m'
    # SELECTED+WHITE+background
    SWHITE_BLACKBG = '\033[7;37;40m'
    SWHITE_REDBG = '\033[7;37;41m'
    SWHITE_GREENBG = '\033[7;37;42m'
    SWHITE_YELLOWBG = '\033[7;37;43m'
    SWHITE_BLUEBG = '\033[7;37;44m'
    SWHITE_VIOLETBG = '\033[7;37;45m'
    SWHITE_CYANBG = '\033[7;37;46m'
    SWHITE_WHITEBG = '\033[7;37;47m'
    SWHITE_GREYBG = '\033[7;37;100m'
    # SELECTED+GREY+background
    SGREY_BLACKBG = '\033[7;90;40m'
    SGREY_REDBG = '\033[7;90;41m'
    SGREY_GREENBG = '\033[7;90;42m'
    SGREY_YELLOWBG = '\033[7;90;43m'
    SGREY_BLUEBG = '\033[7;90;44m'
    SGREY_VIOLETBG = '\033[7;90;45m'
    SGREY_CYANBG = '\033[7;90;46m'
    SGREY_WHITEBG = '\033[7;90;47m'
    SGREY_GREYBG = '\033[7;90;100m'