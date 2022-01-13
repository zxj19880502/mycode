# -*- coding: utf-8 -*-

parameterHeaderSingle = ["time", "model", "fluxsolder", "fluxspeed", "fluxcnywidth", "spraylength", "spraywidth",
                    "nozzlespeed", "spraypress", "solderflow", "solderproportion", "wsspeed", "wscnywidth",
                    "PreheatZone1", "PreheatZone2", "PreheatZone3", "stp", "wave1motor", "wave2motor",
                    "wave1height", "wave2height", "cnyangle"]
parameterHeader = {
            ("D07", "MP18", "MP-TJ-ATM-065"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-CNY-028"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-CNY-104"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-WLD-054"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-ATM-066"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-CNY-026"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-CNY-029"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-GLU-043"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D07", "MP18", "MP-TJ-ATM-107"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"]
           }

errCodeLength = 16
errcodeDict = {
    ("D07", "MP18", "MP-TJ-CNY-028"):{},
    ("D07", "MP18", "MP-TJ-CNY-104"):{},
    ("D07", "MP18", "MP-TJ-CNY-026"):{},
    ("D07", "MP18", "MP-TJ-CNY-029"):{},
      ("D07", "MP18","MP-TJ-ATM-065"): {
        "D2000": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A人工位顶升气缸异常报警"
        }, 
        "D2001": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B人工位顶升气缸异常报警"
        }, 
        "D2002": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A升降机气缸异常报警"
        }, 
        "D2003": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B升降机气缸异常报警"
        }, 
        "D2004": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A升降机运转超时"
        }, 
        "D2005": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B升降机运转超时"
        }, 
        "D2006": {
            "alias": "", 
            "tag": 1, 
            "desc": "升降机门控报警、"
        }, 
        "D2007": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B升降机平台保护光电报警"
        }, 
        "D2008": {
            "alias": "", 
            "tag": 1, 
            "desc": "升降机保护光栅报警"
        }
    }, 
    ("D07", "MP18","MP-TJ-WLD-054"): {
        "D2000": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event0"
        }, 
        "D2001": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event1"
        }, 
        "D2002": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event2"
        }, 
        "D2003": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event3"
        }, 
        "D2004": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event4"
        }, 
        "D2005": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event5"
        }, 
        "D2006": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event6"
        }, 
        "D2007": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event7"
        }, 
        "D2008": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event8"
        }, 
        "D2009": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event9"
        }, 
        "D2010": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event10"
        }, 
        "D2011": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event11"
        }, 
        "D2012": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event12"
        }, 
        "D2013": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event13"
        }, 
        "D2014": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event14"
        }, 
        "D2015": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event15"
        }, 
        "D2016": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event16"
        }, 
        "D2017": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event17"
        }, 
        "D2018": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event18"
        }, 
        "D2019": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event19"
        }, 
        "D2020": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event20"
        }, 
        "D2021": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event21"
        }, 
        "D2022": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event22"
        }, 
        "D2023": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event23"
        }, 
        "D2024": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event24"
        }, 
        "D2025": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event25"
        }, 
        "D2026": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event26"
        }, 
        "D2027": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event27"
        }, 
        "D2028": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event28"
        }, 
        "D2029": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event29"
        }, 
        "D2030": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event30"
        }, 
        "D2031": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event31"
        }, 
        "D2032": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event32"
        }, 
        "D2033": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event33"
        }, 
        "D2034": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event34"
        }, 
        "D2035": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event35"
        }, 
        "D2036": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event36"
        }, 
        "D2037": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event37"
        }, 
        "D2038": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event38"
        }, 
        "D2039": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event39"
        }, 
        "D2040": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event40"
        }, 
        "D2041": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event41"
        }, 
        "D2042": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event42"
        }, 
        "D2043": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event43"
        }, 
        "D2044": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event44"
        }, 
        "D2045": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event45"
        }, 
        "D2046": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event46"
        }, 
        "D2047": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event47"
        }, 
        "D2048": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event48"
        }, 
        "D2049": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event49"
        }, 
        "D2050": {
            "alias": "", 
            "tag": 1, 
            "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2051": {
            "alias": "", 
            "tag": 1, 
            "desc": " 焊锡安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2052": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event52"
        }, 
        "D2053": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event53"
        }, 
        "D2054": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event54"
        }, 
        "D2055": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event55"
        }, 
        "D2056": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event56"
        }, 
        "D2057": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
        }, 
        "D2058": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
        }, 
        "D2059": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
        }, 
        "D2060": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event60"
        }, 
        "D2061": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event61"
        }, 
        "D2062": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event62"
        }, 
        "D2063": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event63"
        }, 
        "D2064": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event64"
        }, 
        "D2065": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event65"
        }, 
        "D2066": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event66"
        }, 
        "D2067": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event67"
        }, 
        "D2068": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event68"
        }, 
        "D2069": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event69"
        }, 
        "D2070": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event70"
        }, 
        "D2071": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event71"
        }, 
        "D2072": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event72"
        }, 
        "D2073": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event73"
        }, 
        "D2074": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event74"
        }, 
        "D2075": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event75"
        }, 
        "D2076": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event76"
        }, 
        "D2077": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event77"
        }, 
        "D2078": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event78"
        }, 
        "D2079": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event79"
        }, 
        "D2080": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event80"
        }, 
        "D2081": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event81"
        }, 
        "D2082": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event82"
        }, 
        "D2083": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event83"
        }, 
        "D2084": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event84"
        }, 
        "D2085": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event85"
        }, 
        "D2086": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event86"
        }, 
        "D2087": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event87"
        }, 
        "D2088": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event88"
        }, 
        "D2089": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event89"
        }, 
        "D2090": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event90"
        }, 
        "D2091": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event91"
        }, 
        "D2092": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event92"
        }, 
        "D2093": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event93"
        }, 
        "D2094": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event94"
        }, 
        "D2095": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event95"
        }, 
        "D2096": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event96"
        }, 
        "D2097": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event97"
        }, 
        "D2098": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event98"
        }, 
        "D2099": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event99"
        }, 
        "D2100": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event100"
        }, 
        "D2101": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升气缸上升异常，请检查Y21、X31"
        }, 
        "D2102": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升气缸下降异常，请检查Y22、X32"
        }, 
        "D2103": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升气缸异常，请检查X31、X32"
        }, 
        "D2104": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升气缸上升异常，请检查Y25、X35"
        }, 
        "D2105": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升气缸下降异常，请检查Y26、X36"
        }, 
        "D2106": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升气缸异常，请检查X35、X36"
        }, 
        "D2107": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event107"
        }, 
        "D2108": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event108"
        }, 
        "D2109": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event109"
        }, 
        "D2110": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A到位阻挡下降超时"
        }, 
        "D2111": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B到位阻挡下降超时"
        }, 
        "D2112": {
            "alias": "", 
            "tag": 1, 
            "desc": " 烙铁头1到达最大使用次数，请更换"
        }, 
        "D2113": {
            "alias": "", 
            "tag": 1, 
            "desc": " 烙铁头2到达最大使用次数，请更换"
        }, 
        "D2114": {
            "alias": "", 
            "tag": 1, 
            "desc": " 机械手送锡步进1缺锡检测报警"
        }, 
        "D2115": {
            "alias": "", 
            "tag": 1, 
            "desc": " 机械手送锡步进1堵锡检测报警"
        }, 
        "D2116": {
            "alias": "", 
            "tag": 1, 
            "desc": " 机械手送锡步进2缺锡检测报警"
        }, 
        "D2117": {
            "alias": "", 
            "tag": 1, 
            "desc": " 机械手送锡步进2堵锡检测报警"
        }, 
        "D2118": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A压条限高异常报警，请检查压条是否装好！"
        }, 
        "D2119": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B压条限高异常报警，请检查压条是否装好！"
        }, 
        "D2120": {
            "alias": "", 
            "tag": 1, 
            "desc": " 烙铁寿命到达设定次数，请确认！"
        }, 
        "D2121": {
            "alias": "", 
            "tag": 1, 
            "desc": " 烙铁未打开报警，请确认！检查输出Y17是否有输出！_x000D_\n点击复位按键清除报警！"
        }, 
        "D2122": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event122"
        }, 
        "D2123": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event123"
        }, 
        "D2124": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event124"
        }, 
        "D2125": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event125"
        }, 
        "D2126": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event126"
        }, 
        "D2127": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event127"
        }, 
        "D2128": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event128"
        }, 
        "D2129": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event129"
        }, 
        "D2130": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-1-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2131": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-2-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2132": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-1-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2133": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-2-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2134": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event134"
        }, 
        "D2135": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-1-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2136": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-2-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2137": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-1-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2138": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-2-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
        }, 
        "D2139": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event139"
        }, 
        "D2140": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-1-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
        }, 
        "D2141": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A焊点-2-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
        }, 
        "D2142": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-1-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
        }, 
        "D2143": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B焊点-2-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
        }, 
        "D2144": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event144"
        }, 
        "D2145": {
            "alias": "", 
            "tag": 1, 
            "desc": " 焊锡机械手不在安全位置，X-Y的定位输出位置超出1.5CM,_x000D_\n请记录异常解除里相关信息，请复位设备，以及检查焊点位置是否准确！"
        }, 
        "D2146": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event146"
        }, 
        "D2147": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event147"
        }, 
        "D2148": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event148"
        }, 
        "D2149": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event149"
        }, 
        "D2150": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event150"
        }, 
        "D2151": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event151"
        }, 
        "D2152": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event152"
        }, 
        "D2153": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event153"
        }, 
        "D2154": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event154"
        }, 
        "D2155": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event155"
        }, 
        "D2156": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event156"
        }, 
        "D2157": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event157"
        }, 
        "D2158": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event158"
        }, 
        "D2159": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event159"
        }, 
        "D2160": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event160"
        }, 
        "D2161": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event161"
        }, 
        "D2162": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event162"
        }, 
        "D2163": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event163"
        }, 
        "D2164": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event164"
        }, 
        "D2165": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event165"
        }, 
        "D2166": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event166"
        }, 
        "D2167": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event167"
        }, 
        "D2168": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event168"
        }, 
        "D2169": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event169"
        }, 
        "D2170": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event170"
        }, 
        "D2171": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event171"
        }, 
        "D2172": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event172"
        }, 
        "D2173": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event173"
        }, 
        "D2174": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event174"
        }, 
        "D2175": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event175"
        }, 
        "D2176": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event176"
        }, 
        "D2177": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event177"
        }, 
        "D2178": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event178"
        }, 
        "D2179": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event179"
        }, 
        "D2180": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event180"
        }, 
        "D2181": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event181"
        }, 
        "D2182": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event182"
        }, 
        "D2183": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event183"
        }, 
        "D2184": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event184"
        }, 
        "D2185": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event185"
        }, 
        "D2186": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event186"
        }, 
        "D2187": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event187"
        }, 
        "D2188": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event188"
        }, 
        "D2189": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event189"
        }, 
        "D2190": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event190"
        }, 
        "D2191": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event191"
        }, 
        "D2192": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event192"
        }, 
        "D2193": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event193"
        }, 
        "D2194": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event194"
        }, 
        "D2195": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event195"
        }, 
        "D2196": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event196"
        }, 
        "D2197": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event197"
        }, 
        "D2198": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event198"
        }, 
        "D2199": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event199"
        }, 
        "D2200": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event200"
        }, 
        "D2201": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event201"
        }, 
        "D2202": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event202"
        }, 
        "D2203": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event203"
        }, 
        "D2204": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event204"
        }, 
        "D2205": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event205"
        }, 
        "D2206": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event206"
        }, 
        "D2207": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event207"
        }, 
        "D2208": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event208"
        }, 
        "D2209": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event209"
        }, 
        "D2210": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event210"
        }, 
        "D2211": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event211"
        }, 
        "D2212": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event212"
        }, 
        "D2213": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event213"
        }, 
        "D2214": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event214"
        }, 
        "D2215": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event215"
        }, 
        "D2216": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event216"
        }, 
        "D2217": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event217"
        }, 
        "D2218": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event218"
        }, 
        "D2219": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event219"
        }, 
        "D2220": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event220"
        }, 
        "D2221": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event221"
        }, 
        "D2222": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event222"
        }, 
        "D2223": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event223"
        }, 
        "D2224": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event224"
        }, 
        "D2225": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event225"
        }, 
        "D2226": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event226"
        }, 
        "D2227": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event227"
        }, 
        "D2228": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event228"
        }, 
        "D2229": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event229"
        }, 
        "D2230": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event230"
        }, 
        "D2231": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event231"
        }, 
        "D2232": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event232"
        }, 
        "D2233": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event233"
        }, 
        "D2234": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event234"
        }, 
        "D2235": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event235"
        }, 
        "D2236": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event236"
        }, 
        "D2237": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event237"
        }, 
        "D2238": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event238"
        }, 
        "D2239": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event239"
        }, 
        "D2240": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event240"
        }, 
        "D2241": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event241"
        }, 
        "D2242": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event242"
        }, 
        "D2243": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event243"
        }, 
        "D2244": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event244"
        }, 
        "D2245": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event245"
        }, 
        "D2246": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event246"
        }, 
        "D2247": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event247"
        }, 
        "D2248": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event248"
        }, 
        "D2249": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event249"
        }, 
        "D2250": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event250"
        }, 
        "D2251": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event251"
        }, 
        "D2252": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event252"
        }, 
        "D2253": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event253"
        }, 
        "D2254": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event254"
        }, 
        "D2255": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event255"
        }, 
        "D2256": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event256"
        }, 
        "D2257": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event257"
        }, 
        "D2258": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event258"
        }, 
        "D2259": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event259"
        }, 
        "D2260": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event260"
        }, 
        "D2261": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event261"
        }, 
        "D2262": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event262"
        }, 
        "D2263": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event263"
        }, 
        "D2264": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event264"
        }, 
        "D2265": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event265"
        }, 
        "D2266": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event266"
        }, 
        "D2267": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event267"
        }, 
        "D2268": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event268"
        }, 
        "D2269": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event269"
        }, 
        "D2270": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event270"
        }, 
        "D2271": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event271"
        }, 
        "D2272": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event272"
        }, 
        "D2273": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event273"
        }, 
        "D2274": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event274"
        }, 
        "D2275": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event275"
        }, 
        "D2276": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event276"
        }, 
        "D2277": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event277"
        }, 
        "D2278": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event278"
        }, 
        "D2279": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event279"
        }, 
        "D2280": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event280"
        }, 
        "D2281": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event281"
        }, 
        "D2282": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event282"
        }, 
        "D2283": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event283"
        }, 
        "D2284": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event284"
        }, 
        "D2285": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event285"
        }, 
        "D2286": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event286"
        }, 
        "D2287": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event287"
        }, 
        "D2288": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event288"
        }, 
        "D2289": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event289"
        }, 
        "D2290": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event290"
        }, 
        "D2291": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event291"
        }, 
        "D2292": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event292"
        }, 
        "D2293": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event293"
        }, 
        "D2294": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event294"
        }, 
        "D2295": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event295"
        }, 
        "D2296": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event296"
        }, 
        "D2297": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event297"
        }, 
        "D2298": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event298"
        }, 
        "D2299": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event299"
        }, 
        "D2300": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event300"
        }
    }, 
    ("D07", "MP18","MP-TJ-ATM-066"): {
        "D2000": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event0"
        }, 
        "D2001": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event1"
        }, 
        "D2002": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event2"
        }, 
        "D2003": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event3"
        }, 
        "D2004": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event4"
        }, 
        "D2005": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event5"
        }, 
        "D2006": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event6"
        }, 
        "D2007": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event7"
        }, 
        "D2008": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event8"
        }, 
        "D2009": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event9"
        }, 
        "D2010": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event10"
        }, 
        "D2011": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event11"
        }, 
        "D2012": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event12"
        }, 
        "D2013": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event13"
        }, 
        "D2014": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event14"
        }, 
        "D2015": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event15"
        }, 
        "D2016": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event16"
        }, 
        "D2017": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event17"
        }, 
        "D2018": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event18"
        }, 
        "D2019": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event19"
        }, 
        "D2020": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event20"
        }, 
        "D2021": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event21"
        }, 
        "D2022": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event22"
        }, 
        "D2023": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event23"
        }, 
        "D2024": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event24"
        }, 
        "D2025": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event25"
        }, 
        "D2026": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event26"
        }, 
        "D2027": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event27"
        }, 
        "D2028": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event28"
        }, 
        "D2029": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event29"
        }, 
        "D2030": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event30"
        }, 
        "D2031": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event31"
        }, 
        "D2032": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event32"
        }, 
        "D2033": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event33"
        }, 
        "D2034": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event34"
        }, 
        "D2035": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event35"
        }, 
        "D2036": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event36"
        }, 
        "D2037": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event37"
        }, 
        "D2038": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event38"
        }, 
        "D2039": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event39"
        }, 
        "D2040": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event40"
        }, 
        "D2041": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event41"
        }, 
        "D2042": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event42"
        }, 
        "D2043": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event43"
        }, 
        "D2044": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event44"
        }, 
        "D2045": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event45"
        }, 
        "D2046": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event46"
        }, 
        "D2047": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event47"
        }, 
        "D2048": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event48"
        }, 
        "D2049": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event49"
        }, 
        "D2050": {
            "alias": "", 
            "tag": 1, 
            "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2051": {
            "alias": "", 
            "tag": 1, 
            "desc": " 安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2052": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event52"
        }, 
        "D2053": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event53"
        }, 
        "D2054": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event54"
        }, 
        "D2055": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event55"
        }, 
        "D2056": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event56"
        }, 
        "D2057": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
        }, 
        "D2058": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
        }, 
        "D2059": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
        }, 
        "D2060": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event60"
        }, 
        "D2061": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event61"
        }, 
        "D2062": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event62"
        }, 
        "D2063": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event63"
        }, 
        "D2064": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event64"
        }, 
        "D2065": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event65"
        }, 
        "D2066": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event66"
        }, 
        "D2067": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event67"
        }, 
        "D2068": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event68"
        }, 
        "D2069": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event69"
        }, 
        "D2070": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event70"
        }, 
        "D2071": {
            "alias": "", 
            "tag": 1, 
            "desc": " 设备伺服报警，请检查伺服驱动器的报错代码"
        }, 
        "D2072": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event72"
        }, 
        "D2073": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event73"
        }, 
        "D2074": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event74"
        }, 
        "D2075": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event75"
        }, 
        "D2076": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event76"
        }, 
        "D2077": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event77"
        }, 
        "D2078": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event78"
        }, 
        "D2079": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event79"
        }, 
        "D2080": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event80"
        }, 
        "D2081": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event81"
        }, 
        "D2082": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event82"
        }, 
        "D2083": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event83"
        }, 
        "D2084": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event84"
        }, 
        "D2085": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event85"
        }, 
        "D2086": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event86"
        }, 
        "D2087": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event87"
        }, 
        "D2088": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event88"
        }, 
        "D2089": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event89"
        }, 
        "D2090": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event90"
        }, 
        "D2091": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event91"
        }, 
        "D2092": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event92"
        }, 
        "D2093": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event93"
        }, 
        "D2094": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event94"
        }, 
        "D2095": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event95"
        }, 
        "D2096": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event96"
        }, 
        "D2097": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event97"
        }, 
        "D2098": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event98"
        }, 
        "D2099": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event99"
        }, 
        "D2100": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event100"
        }, 
        "D2101": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位顶升气缸上升异常，请查看输入“X32”或输出“Y32”"
        }, 
        "D2102": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位顶升气缸下降异常，请查看输入“X33”或输出“Y33”"
        }, 
        "D2103": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位顶升气缸感应异常，请查看输入“X32”或“X33”"
        }, 
        "D2104": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位定位气缸伸出异常，请查看输入“X34 X36”或输出“Y34”"
        }, 
        "D2105": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位定位气缸退回异常，请查看输入“X35 X37”或输出“Y35”"
        }, 
        "D2106": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位定位气缸异常，请查看输入“X35 X37 X34 X36”"
        }, 
        "D2107": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位下机芯位治具旋转气缸旋转异常，请查看输入“X40 X42”或输出“Y36”"
        }, 
        "D2108": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位下机芯位治具旋转气缸复位异常，请查看输入“X41 X43”或输出“Y37”"
        }, 
        "D2109": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A下机芯位下机芯位治具旋转气缸异常，请查看输入“X41 X42 X43 X40”"
        }, 
        "D2110": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A放行超时，请检查是否卡治具！"
        }, 
        "D2111": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位顶升气缸上升异常，请查看输入“X45”或输出“Y41”"
        }, 
        "D2112": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位顶升气缸下降异常，请查看输入“X46”或输出“Y42”"
        }, 
        "D2113": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位顶升气缸感应异常，请查看输入“X45”或“X46”"
        }, 
        "D2114": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位定位气缸伸出异常，请查看输入“X47 X51”或输出“Y43”"
        }, 
        "D2115": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位定位气缸退回异常，请查看输入“X50 X52”或输出“Y44”"
        }, 
        "D2116": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位定位气缸异常，请查看输入“X47 X50 X51 X52”"
        }, 
        "D2117": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位下机芯位治具旋转气缸旋转异常，请查看输入“X53 X55”或输出“Y45”"
        }, 
        "D2118": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位下机芯位治具旋转气缸复位异常，请查看输入“X54 X56”或输出“Y46”"
        }, 
        "D2119": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B下机芯位下机芯位治具旋转气缸异常，请查看输入“X53 X54 X55 X56”"
        }, 
        "D2120": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2121": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event121"
        }, 
        "D2122": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event122"
        }, 
        "D2123": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event123"
        }, 
        "D2124": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event124"
        }, 
        "D2125": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2126": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event126"
        }, 
        "D2127": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event127"
        }, 
        "D2128": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event128"
        }, 
        "D2129": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2130": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2131": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件上下气缸上升异常，请查看输入“X71 X73”或输出“Y55”"
        }, 
        "D2132": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件上下气缸下降异常，请查看输入“X70 X72”或输出“Y54”"
        }, 
        "D2133": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件上下气缸异常，请查看输入“X70 X71 X72 X73”"
        }, 
        "D2134": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件夹爪气缸松开异常，请查看输入“X74 X75”或输出“Y57”"
        }, 
        "D2135": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件夹爪气缸夹紧异常，请查看输入“X74 X75”或输出“Y56”"
        }, 
        "D2136": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹压件夹爪气缸异常，请查看输入“X74 X75”"
        }, 
        "D2137": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹PCB夹爪气缸松开异常，请查看输入“X76 X77”或输出“Y61”"
        }, 
        "D2138": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹PCB夹爪气缸夹紧异常，请查看输入“X76 X77”或输出“Y60”"
        }, 
        "D2139": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A机械手夹PCB夹爪气缸异常，请查看输入“X76 X77”"
        }, 
        "D2140": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B放行超时，请检查是否卡治具！"
        }, 
        "D2141": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件上下气缸上升异常，请查看输入“X81 X83”或输出“Y65”"
        }, 
        "D2142": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件上下气缸下降异常，请查看输入“X80 X82”或输出“Y64”"
        }, 
        "D2143": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件上下气缸异常，请查看输入“X80 X81 X82 X83”"
        }, 
        "D2144": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件夹爪气缸松开异常，请查看输入“X84 X85”或输出“Y67”"
        }, 
        "D2145": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件夹爪气缸夹紧异常，请查看输入“X84 X85”或输出“Y66”"
        }, 
        "D2146": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹压件夹爪气缸异常，请查看输入“X84 X85”"
        }, 
        "D2147": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹PCB夹爪气缸松开异常，请查看输入“X86 X87”或输出“Y71”"
        }, 
        "D2148": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹PCB夹爪气缸夹紧异常，请查看输入“X86 X87”或输出“Y80”"
        }, 
        "D2149": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B机械手夹PCB夹爪气缸异常，请查看输入“X86 X87”"
        }, 
        "D2150": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event150"
        }, 
        "D2151": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2152": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2153": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2154": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2155": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2156": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2157": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2158": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2159": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2160": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2161": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2162": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2163": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event163"
        }, 
        "D2164": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event164"
        }, 
        "D2165": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event165"
        }, 
        "D2166": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event166"
        }, 
        "D2167": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event167"
        }, 
        "D2168": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event168"
        }, 
        "D2169": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event169"
        }, 
        "D2170": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event170"
        }, 
        "D2171": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2172": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2173": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2174": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2175": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event175"
        }, 
        "D2176": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event176"
        }, 
        "D2177": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event177"
        }, 
        "D2178": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event178"
        }, 
        "D2179": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event179"
        }, 
        "D2180": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event180"
        }, 
        "D2181": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2182": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2183": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2184": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event"
        }, 
        "D2185": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event185"
        }, 
        "D2186": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event186"
        }, 
        "D2187": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event187"
        }, 
        "D2188": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event188"
        }, 
        "D2189": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event189"
        }, 
        "D2190": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event190"
        }, 
        "D2191": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event191"
        }, 
        "D2192": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event192"
        }, 
        "D2193": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event193"
        }, 
        "D2194": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event194"
        }, 
        "D2195": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event195"
        }, 
        "D2196": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event196"
        }, 
        "D2197": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event197"
        }, 
        "D2198": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event198"
        }, 
        "D2199": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event199"
        }, 
        "D2200": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event200"
        }, 
        "D2201": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event201"
        }, 
        "D2202": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event202"
        }, 
        "D2203": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event203"
        }, 
        "D2204": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event204"
        }, 
        "D2205": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event205"
        }, 
        "D2206": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event206"
        }, 
        "D2207": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event207"
        }, 
        "D2208": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event208"
        }, 
        "D2209": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event209"
        }, 
        "D2210": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event210"
        }, 
        "D2211": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event211"
        }, 
        "D2212": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event212"
        }, 
        "D2213": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event213"
        }, 
        "D2214": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event214"
        }, 
        "D2215": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event215"
        }, 
        "D2216": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event216"
        }, 
        "D2217": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event217"
        }, 
        "D2218": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event218"
        }, 
        "D2219": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event219"
        }, 
        "D2220": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event220"
        }, 
        "D2221": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event221"
        }, 
        "D2222": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event222"
        }, 
        "D2223": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event223"
        }, 
        "D2224": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event224"
        }, 
        "D2225": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event225"
        }, 
        "D2226": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event226"
        }, 
        "D2227": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event227"
        }, 
        "D2228": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event228"
        }, 
        "D2229": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event229"
        }, 
        "D2230": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event230"
        }, 
        "D2231": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event231"
        }, 
        "D2232": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event232"
        }, 
        "D2233": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event233"
        }, 
        "D2234": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event234"
        }, 
        "D2235": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event235"
        }, 
        "D2236": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event236"
        }, 
        "D2237": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event237"
        }, 
        "D2238": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event238"
        }, 
        "D2239": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event239"
        }, 
        "D2240": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event240"
        }, 
        "D2241": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event241"
        }, 
        "D2242": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event242"
        }, 
        "D2243": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event243"
        }, 
        "D2244": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event244"
        }, 
        "D2245": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event245"
        }, 
        "D2246": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event246"
        }, 
        "D2247": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event247"
        }, 
        "D2248": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event248"
        }, 
        "D2249": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event249"
        }, 
        "D2250": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event250"
        }, 
        "D2251": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event251"
        }, 
        "D2252": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event252"
        }, 
        "D2253": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event253"
        }, 
        "D2254": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event254"
        }, 
        "D2255": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event255"
        }, 
        "D2256": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event256"
        }, 
        "D2257": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event257"
        }, 
        "D2258": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event258"
        }, 
        "D2259": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event259"
        }, 
        "D2260": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event260"
        }, 
        "D2261": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event261"
        }, 
        "D2262": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event262"
        }, 
        "D2263": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event263"
        }, 
        "D2264": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event264"
        }, 
        "D2265": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event265"
        }, 
        "D2266": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event266"
        }, 
        "D2267": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event267"
        }, 
        "D2268": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event268"
        }, 
        "D2269": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event269"
        }, 
        "D2270": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event270"
        }, 
        "D2271": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event271"
        }, 
        "D2272": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event272"
        }, 
        "D2273": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event273"
        }, 
        "D2274": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event274"
        }, 
        "D2275": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event275"
        }, 
        "D2276": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event276"
        }, 
        "D2277": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event277"
        }, 
        "D2278": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event278"
        }, 
        "D2279": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event279"
        }, 
        "D2280": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event280"
        }, 
        "D2281": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event281"
        }, 
        "D2282": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event282"
        }, 
        "D2283": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event283"
        }, 
        "D2284": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event284"
        }, 
        "D2285": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event285"
        }, 
        "D2286": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event286"
        }, 
        "D2287": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event287"
        }, 
        "D2288": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event288"
        }, 
        "D2289": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event289"
        }, 
        "D2290": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event290"
        }, 
        "D2291": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event291"
        }, 
        "D2292": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event292"
        }, 
        "D2293": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event293"
        }, 
        "D2294": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event294"
        }, 
        "D2295": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event295"
        }, 
        "D2296": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event296"
        }, 
        "D2297": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event297"
        }, 
        "D2298": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event298"
        }, 
        "D2299": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event299"
        }
    }, 
    ("D07", "MP18","MP-TJ-GLU-043"): {
        "D2000": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event0"
        }, 
        "D2001": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event1"
        }, 
        "D2002": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event2"
        }, 
        "D2003": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event3"
        }, 
        "D2004": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event4"
        }, 
        "D2005": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event5"
        }, 
        "D2006": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event6"
        }, 
        "D2007": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event7"
        }, 
        "D2008": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event8"
        }, 
        "D2009": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event9"
        }, 
        "D2010": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event10"
        }, 
        "D2011": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event11"
        }, 
        "D2012": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event12"
        }, 
        "D2013": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event13"
        }, 
        "D2014": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event14"
        }, 
        "D2015": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event15"
        }, 
        "D2016": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event16"
        }, 
        "D2017": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event17"
        }, 
        "D2018": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event18"
        }, 
        "D2019": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event19"
        }, 
        "D2020": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event20"
        }, 
        "D2021": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event21"
        }, 
        "D2022": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event22"
        }, 
        "D2023": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event23"
        }, 
        "D2024": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event24"
        }, 
        "D2025": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event25"
        }, 
        "D2026": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event26"
        }, 
        "D2027": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event27"
        }, 
        "D2028": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event28"
        }, 
        "D2029": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event29"
        }, 
        "D2030": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event30"
        }, 
        "D2031": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event31"
        }, 
        "D2032": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event32"
        }, 
        "D2033": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event33"
        }, 
        "D2034": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event34"
        }, 
        "D2035": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event35"
        }, 
        "D2036": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event36"
        }, 
        "D2037": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event37"
        }, 
        "D2038": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event38"
        }, 
        "D2039": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event39"
        }, 
        "D2040": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event40"
        }, 
        "D2041": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event41"
        }, 
        "D2042": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event42"
        }, 
        "D2043": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event43"
        }, 
        "D2044": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event44"
        }, 
        "D2045": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event45"
        }, 
        "D2046": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event46"
        }, 
        "D2047": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event47"
        }, 
        "D2048": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event48"
        }, 
        "D2049": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event49"
        }, 
        "D2050": {
            "alias": "", 
            "tag": 1, 
            "desc": "紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2051": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶工位安全门打开_x000D_\n请人工确认"
        }, 
        "D2052": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶工位安全门打开_x000D_\n请人工确认"
        }, 
        "D2053": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event53"
        }, 
        "D2054": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event54"
        }, 
        "D2055": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event55"
        }, 
        "D2056": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event56"
        }, 
        "D2057": {
            "alias": "", 
            "tag": 1, 
            "desc": "与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
        }, 
        "D2058": {
            "alias": "", 
            "tag": 1, 
            "desc": "与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
        }, 
        "D2059": {
            "alias": "", 
            "tag": 1, 
            "desc": "与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
        }, 
        "D2060": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event60"
        }, 
        "D2061": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event61"
        }, 
        "D2062": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event62"
        }, 
        "D2063": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event63"
        }, 
        "D2064": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event64"
        }, 
        "D2065": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工段远程模块连接失败，请检查，后断电重启！！"
        }, 
        "D2066": {
            "alias": "", 
            "tag": 1, 
            "desc": "当前机种编号与记忆机种不一致，请检查，及时调取或者保存参数"
        }, 
        "D2067": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event67"
        }, 
        "D2068": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event68"
        }, 
        "D2069": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event69"
        }, 
        "D2070": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event70"
        }, 
        "D2071": {
            "alias": "", 
            "tag": 1, 
            "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
        }, 
        "D2072": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event72"
        }, 
        "D2073": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event73"
        }, 
        "D2074": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event74"
        }, 
        "D2075": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event75"
        }, 
        "D2076": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event76"
        }, 
        "D2077": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event77"
        }, 
        "D2078": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event78"
        }, 
        "D2079": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event79"
        }, 
        "D2080": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event80"
        }, 
        "D2081": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event81"
        }, 
        "D2082": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event82"
        }, 
        "D2083": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event83"
        }, 
        "D2084": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event84"
        }, 
        "D2085": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event85"
        }, 
        "D2086": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event86"
        }, 
        "D2087": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event87"
        }, 
        "D2088": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event88"
        }, 
        "D2089": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event89"
        }, 
        "D2090": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event90"
        }, 
        "D2091": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event91"
        }, 
        "D2092": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event92"
        }, 
        "D2093": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event93"
        }, 
        "D2094": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event94"
        }, 
        "D2095": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event95"
        }, 
        "D2096": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event96"
        }, 
        "D2097": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event97"
        }, 
        "D2098": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event98"
        }, 
        "D2099": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event99"
        }, 
        "D2100": {
            "alias": "", 
            "tag": 1, 
            "desc": "伺服在线失败，请检查！"
        }, 
        "D2101": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
        }, 
        "D2102": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
        }, 
        "D2103": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
        }, 
        "D2104": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
        }, 
        "D2105": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
        }, 
        "D2106": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X45 下限X46"
        }, 
        "D2107": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
        }, 
        "D2108": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
        }, 
        "D2109": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X62 下限X63"
        }, 
        "D2110": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
        }, 
        "D2111": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
        }, 
        "D2112": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X75 下限X76"
        }, 
        "D2113": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A产品检测异常"
        }, 
        "D2114": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B产品检测异常"
        }, 
        "D2115": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶前检测产品有浮高，请人工确认"
        }, 
        "D2116": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event116"
        }, 
        "D2117": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event117"
        }, 
        "D2118": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道A升降机气缸上限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
        }, 
        "D2119": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道A升降机气缸下限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
        }, 
        "D2120": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道A升降机气缸报警，请检查IO 上限X220 下限X221"
        }, 
        "D2121": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道B升降机气缸上限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
        }, 
        "D2122": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道B升降机气缸下限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
        }, 
        "D2123": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道B升降机气缸报警，请检查IO 上限X226 下限X227"
        }, 
        "D2124": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道A步进马达运转超时"
        }, 
        "D2125": {
            "alias": "", 
            "tag": 1, 
            "desc": "人工位轨道B步进马达运转超时"
        }, 
        "D2126": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event126"
        }, 
        "D2127": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event127"
        }, 
        "D2128": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event128"
        }, 
        "D2129": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event129"
        }, 
        "D2130": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道A入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
        }, 
        "D2131": {
            "alias": "", 
            "tag": 1, 
            "desc": "轨道B入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
        }, 
        "D2132": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event132"
        }, 
        "D2133": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event133"
        }, 
        "D2134": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event134"
        }, 
        "D2135": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event135"
        }, 
        "D2136": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event136"
        }, 
        "D2137": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event137"
        }, 
        "D2138": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event138"
        }, 
        "D2139": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event139"
        }, 
        "D2140": {
            "alias": "", 
            "tag": 1, 
            "desc": "胶桶1缺胶检测报警，请及时换胶！"
        }, 
        "D2141": {
            "alias": "", 
            "tag": 1, 
            "desc": "胶桶2缺胶检测报警，请及时换胶！"
        }, 
        "D2142": {
            "alias": "", 
            "tag": 1, 
            "desc": "胶桶3缺胶检测报警，请及时换胶！"
        }, 
        "D2143": {
            "alias": "", 
            "tag": 1, 
            "desc": "胶桶4缺胶检测报警，请及时换胶！"
        }, 
        "D2144": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event144"
        }, 
        "D2145": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event145"
        }, 
        "D2146": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event146"
        }, 
        "D2147": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event147"
        }, 
        "D2148": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event148"
        }, 
        "D2149": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event149"
        }, 
        "D2150": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道A定位气缸松开异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
        }, 
        "D2151": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道A定位气缸夹紧异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
        }, 
        "D2152": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道A定位气缸夹紧感应X34X36，松开感应X35X37"
        }, 
        "D2153": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道B定位气缸松开异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
        }, 
        "D2154": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道B定位气缸夹紧异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
        }, 
        "D2155": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶1轨道B定位气缸松开感应松开感应X50X52，夹紧感应X47X51"
        }, 
        "D2156": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道A定位气缸松开异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
        }, 
        "D2157": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道A定位气缸夹紧异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
        }, 
        "D2158": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道A定位气缸夹紧感应X64X66，松开感应X65X67"
        }, 
        "D2159": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道B定位气缸松开异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
        }, 
        "D2160": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道B定位气缸夹紧异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
        }, 
        "D2161": {
            "alias": "", 
            "tag": 1, 
            "desc": "点胶2轨道B定位气缸松开感应X80X82，夹紧感应X77X81"
        }, 
        "D2162": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event162"
        }, 
        "D2163": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event163"
        }, 
        "D2164": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event164"
        }, 
        "D2165": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event165"
        }, 
        "D2166": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event166"
        }, 
        "D2167": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event167"
        }, 
        "D2168": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event168"
        }, 
        "D2169": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event169"
        }, 
        "D2170": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event170"
        }, 
        "D2171": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event171"
        }, 
        "D2172": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event172"
        }, 
        "D2173": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event173"
        }, 
        "D2174": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event174"
        }, 
        "D2175": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event175"
        }, 
        "D2176": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event176"
        }, 
        "D2177": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event177"
        }, 
        "D2178": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event178"
        }, 
        "D2179": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event179"
        }, 
        "D2180": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event180"
        }, 
        "D2181": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event181"
        }, 
        "D2182": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event182"
        }, 
        "D2183": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event183"
        }, 
        "D2184": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event184"
        }, 
        "D2185": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event185"
        }, 
        "D2186": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event186"
        }, 
        "D2187": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event187"
        }, 
        "D2188": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event188"
        }, 
        "D2189": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event189"
        }, 
        "D2190": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event190"
        }, 
        "D2191": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event191"
        }, 
        "D2192": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event192"
        }, 
        "D2193": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event193"
        }, 
        "D2194": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event194"
        }, 
        "D2195": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event195"
        }, 
        "D2196": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event196"
        }, 
        "D2197": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event197"
        }, 
        "D2198": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event198"
        }, 
        "D2199": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event199"
        }, 
        "D2200": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event200"
        }, 
        "D2201": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event201"
        }, 
        "D2202": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event202"
        }, 
        "D2203": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event203"
        }, 
        "D2204": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event204"
        }, 
        "D2205": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event205"
        }, 
        "D2206": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event206"
        }, 
        "D2207": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event207"
        }, 
        "D2208": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event208"
        }, 
        "D2209": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event209"
        }, 
        "D2210": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event210"
        }, 
        "D2211": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event211"
        }, 
        "D2212": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event212"
        }, 
        "D2213": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event213"
        }, 
        "D2214": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event214"
        }, 
        "D2215": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event215"
        }, 
        "D2216": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event216"
        }, 
        "D2217": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event217"
        }, 
        "D2218": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event218"
        }, 
        "D2219": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event219"
        }, 
        "D2220": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event220"
        }, 
        "D2221": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event221"
        }, 
        "D2222": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event222"
        }, 
        "D2223": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event223"
        }, 
        "D2224": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event224"
        }, 
        "D2225": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event225"
        }, 
        "D2226": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event226"
        }, 
        "D2227": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event227"
        }, 
        "D2228": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event228"
        }, 
        "D2229": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event229"
        }, 
        "D2230": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event230"
        }, 
        "D2231": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event231"
        }, 
        "D2232": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event232"
        }, 
        "D2233": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event233"
        }, 
        "D2234": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event234"
        }, 
        "D2235": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event235"
        }, 
        "D2236": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event236"
        }, 
        "D2237": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event237"
        }, 
        "D2238": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event238"
        }, 
        "D2239": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event239"
        }, 
        "D2240": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event240"
        }, 
        "D2241": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event241"
        }, 
        "D2242": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event242"
        }, 
        "D2243": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event243"
        }, 
        "D2244": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event244"
        }, 
        "D2245": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event245"
        }, 
        "D2246": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event246"
        }, 
        "D2247": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event247"
        }, 
        "D2248": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event248"
        }, 
        "D2249": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event249"
        }, 
        "D2250": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event250"
        }, 
        "D2251": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event251"
        }, 
        "D2252": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event252"
        }, 
        "D2253": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event253"
        }, 
        "D2254": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event254"
        }, 
        "D2255": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event255"
        }, 
        "D2256": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event256"
        }, 
        "D2257": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event257"
        }, 
        "D2258": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event258"
        }, 
        "D2259": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event259"
        }, 
        "D2260": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event260"
        }, 
        "D2261": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event261"
        }, 
        "D2262": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event262"
        }, 
        "D2263": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event263"
        }, 
        "D2264": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event264"
        }, 
        "D2265": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event265"
        }, 
        "D2266": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event266"
        }, 
        "D2267": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event267"
        }, 
        "D2268": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event268"
        }, 
        "D2269": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event269"
        }, 
        "D2270": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event270"
        }, 
        "D2271": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event271"
        }, 
        "D2272": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event272"
        }, 
        "D2273": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event273"
        }, 
        "D2274": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event274"
        }, 
        "D2275": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event275"
        }, 
        "D2276": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event276"
        }, 
        "D2277": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event277"
        }, 
        "D2278": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event278"
        }, 
        "D2279": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event279"
        }, 
        "D2280": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event280"
        }, 
        "D2281": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event281"
        }, 
        "D2282": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event282"
        }, 
        "D2283": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event283"
        }, 
        "D2284": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event284"
        }, 
        "D2285": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event285"
        }, 
        "D2286": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event286"
        }, 
        "D2287": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event287"
        }, 
        "D2288": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event288"
        }, 
        "D2289": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event289"
        }, 
        "D2290": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event290"
        }, 
        "D2291": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event291"
        }, 
        "D2292": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event292"
        }, 
        "D2293": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event293"
        }, 
        "D2294": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event294"
        }, 
        "D2295": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event295"
        }, 
        "D2296": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event296"
        }, 
        "D2297": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event297"
        }, 
        "D2298": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event298"
        }, 
        "D2299": {
            "alias": "", 
            "tag": 1, 
            "desc": "Event299"
        }
    }, 
    ("D07", "MP18","MP-TJ-ATM-107"): {
        "D2000": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event0"
        }, 
        "D2001": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event1"
        }, 
        "D2002": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event2"
        }, 
        "D2003": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event3"
        }, 
        "D2004": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event4"
        }, 
        "D2005": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event5"
        }, 
        "D2006": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event6"
        }, 
        "D2007": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event7"
        }, 
        "D2008": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event8"
        }, 
        "D2009": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event9"
        }, 
        "D2010": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event10"
        }, 
        "D2011": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event11"
        }, 
        "D2012": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event12"
        }, 
        "D2013": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event13"
        }, 
        "D2014": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event14"
        }, 
        "D2015": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event15"
        }, 
        "D2016": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event16"
        }, 
        "D2017": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event17"
        }, 
        "D2018": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event18"
        }, 
        "D2019": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event19"
        }, 
        "D2020": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event20"
        }, 
        "D2021": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event21"
        }, 
        "D2022": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event22"
        }, 
        "D2023": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event23"
        }, 
        "D2024": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event24"
        }, 
        "D2025": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event25"
        }, 
        "D2026": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event26"
        }, 
        "D2027": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event27"
        }, 
        "D2028": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event28"
        }, 
        "D2029": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event29"
        }, 
        "D2030": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event30"
        }, 
        "D2031": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event31"
        }, 
        "D2032": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event32"
        }, 
        "D2033": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event33"
        }, 
        "D2034": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event34"
        }, 
        "D2035": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event35"
        }, 
        "D2036": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event36"
        }, 
        "D2037": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event37"
        }, 
        "D2038": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event38"
        }, 
        "D2039": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event39"
        }, 
        "D2040": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event40"
        }, 
        "D2041": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event41"
        }, 
        "D2042": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event42"
        }, 
        "D2043": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event43"
        }, 
        "D2044": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event44"
        }, 
        "D2045": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event45"
        }, 
        "D2046": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event46"
        }, 
        "D2047": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event47"
        }, 
        "D2048": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event48"
        }, 
        "D2049": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event49"
        }, 
        "D2050": {
            "alias": "", 
            "tag": 1, 
            "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2051": {
            "alias": "", 
            "tag": 1, 
            "desc": " 安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
        }, 
        "D2052": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event52"
        }, 
        "D2053": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event53"
        }, 
        "D2054": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event54"
        }, 
        "D2055": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event55"
        }, 
        "D2056": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event56"
        }, 
        "D2057": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
        }, 
        "D2058": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
        }, 
        "D2059": {
            "alias": "", 
            "tag": 1, 
            "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
        }, 
        "D2060": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event60"
        }, 
        "D2061": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event61"
        }, 
        "D2062": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event62"
        }, 
        "D2063": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event63"
        }, 
        "D2064": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event64"
        }, 
        "D2065": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event65"
        }, 
        "D2066": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event66"
        }, 
        "D2067": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event67"
        }, 
        "D2068": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event68"
        }, 
        "D2069": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event69"
        }, 
        "D2070": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event70"
        }, 
        "D2071": {
            "alias": "", 
            "tag": 1, 
            "desc": " 设备伺服报警，请检查伺服驱动器的报错代码"
        }, 
        "D2072": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event72"
        }, 
        "D2073": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event73"
        }, 
        "D2074": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event74"
        }, 
        "D2075": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event75"
        }, 
        "D2076": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event76"
        }, 
        "D2077": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event77"
        }, 
        "D2078": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event78"
        }, 
        "D2079": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event79"
        }, 
        "D2080": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event80"
        }, 
        "D2081": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event81"
        }, 
        "D2082": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event82"
        }, 
        "D2083": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event83"
        }, 
        "D2084": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event84"
        }, 
        "D2085": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event85"
        }, 
        "D2086": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event86"
        }, 
        "D2087": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event87"
        }, 
        "D2088": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event88"
        }, 
        "D2089": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event89"
        }, 
        "D2090": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event90"
        }, 
        "D2091": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event91"
        }, 
        "D2092": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event92"
        }, 
        "D2093": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event93"
        }, 
        "D2094": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event94"
        }, 
        "D2095": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event95"
        }, 
        "D2096": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event96"
        }, 
        "D2097": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event97"
        }, 
        "D2098": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event98"
        }, 
        "D2099": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event99"
        }, 
        "D2100": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event100"
        }, 
        "D2101": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A升降机上升异常，请检查“X30”或“Y20”，按复位消除报警"
        }, 
        "D2102": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A升降机下降异常，请检查“X31”或“Y21”，按复位消除报警"
        }, 
        "D2103": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A升降机气缸异常报警！请查看X30 X31"
        }, 
        "D2104": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升定位气缸上升异常，请检查“X34”或“Y24”，按复位消除报警"
        }, 
        "D2105": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升定位气缸下降异常，请检查“X35”或“Y25”，按复位消除报警"
        }, 
        "D2106": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A顶升气缸异常报警！请查看X34 X35"
        }, 
        "D2107": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A定位气缸伸出异常，请检查“X36 X40 ” 或“Y26”，按复位消除报警"
        }, 
        "D2108": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A定位气缸退回异常，请检查“X37 X41”或“Y27”，按复位消除报警"
        }, 
        "D2109": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A定位气缸异常报警！！！请查看“X36 X37 X40 X41”"
        }, 
        "D2110": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A旋转气缸旋转异常，请检查“X42 X44”或“Y30”，按复位消除报警"
        }, 
        "D2111": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A旋转气缸复位异常，请检查“X43 X45”或“Y31”，按复位消除报警"
        }, 
        "D2112": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A旋转气缸异常报警！请查看 X42 X43 X44 X45"
        }, 
        "D2113": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event113"
        }, 
        "D2114": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event114"
        }, 
        "D2115": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event115"
        }, 
        "D2116": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event116"
        }, 
        "D2117": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event117"
        }, 
        "D2118": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event118"
        }, 
        "D2119": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event119"
        }, 
        "D2120": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event120"
        }, 
        "D2121": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B升降机上升异常，请检查“X50”或“Y34”，按复位消除报警"
        }, 
        "D2122": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B升降机下降异常，请检查“X51”或“Y35”，按复位消除报警"
        }, 
        "D2123": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B升降机气缸异常报警！请查看X50 X51"
        }, 
        "D2124": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升定位气缸上升异常，请检查“X54”或“Y40”，按复位消除报警"
        }, 
        "D2125": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升定位气缸下降异常，请检查“X55”或“Y41”，按复位消除报警"
        }, 
        "D2126": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B顶升气缸异常报警！请查看X54 X55"
        }, 
        "D2127": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B定位气缸伸出异常，请检查“X56 X60 ” 或“Y42”，按复位消除报警"
        }, 
        "D2128": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B定位气缸退回异常，请检查“X57 X61”或“Y43”，按复位消除报警"
        }, 
        "D2129": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B定位气缸异常报警！！！请查看“X56 X57 X60 X61”"
        }, 
        "D2130": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B旋转气缸旋转异常，请检查“X62 X64”或“Y44”，按复位消除报警"
        }, 
        "D2131": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B旋转气缸复位异常，请检查“X63 X65”或“Y45”，按复位消除报警"
        }, 
        "D2132": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B旋转气缸异常报警！请查看 X62 X63 X64 X65"
        }, 
        "D2133": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event133"
        }, 
        "D2134": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event134"
        }, 
        "D2135": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event135"
        }, 
        "D2136": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event136"
        }, 
        "D2137": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event137"
        }, 
        "D2138": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event138"
        }, 
        "D2139": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event139"
        }, 
        "D2140": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event140"
        }, 
        "D2141": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event141"
        }, 
        "D2142": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event142"
        }, 
        "D2143": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event143"
        }, 
        "D2144": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event144"
        }, 
        "D2145": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event145"
        }, 
        "D2146": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event146"
        }, 
        "D2147": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event147"
        }, 
        "D2148": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event148"
        }, 
        "D2149": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event149"
        }, 
        "D2150": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event150"
        }, 
        "D2151": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪1松开异常，请检查“X61”或“Y60”，按复位消除报警！"
        }, 
        "D2152": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪1夹紧异常，请检查“X61”或“Y60”，按复位消除报警！"
        }, 
        "D2153": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪1气缸异常报警！"
        }, 
        "D2154": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪2松开异常，请检查“X62”或“Y62”，按复位消除报警！"
        }, 
        "D2155": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪2夹紧异常，请检查“X62”或“Y62”，按复位消除报警！"
        }, 
        "D2156": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪2气缸异常报警！"
        }, 
        "D2157": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪3松开异常，请检查“X65”或“Y65”，按复位消除报警！"
        }, 
        "D2158": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪3夹紧异常，请检查“X65”或“Y64”，按复位消除报警！"
        }, 
        "D2159": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪3气缸异常报警！"
        }, 
        "D2160": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪4松开异常，请检查“X67”或“Y67”，按复位消除报警！"
        }, 
        "D2161": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪4夹紧异常，请检查“X67”或“Y66”，按复位消除报警！"
        }, 
        "D2162": {
            "alias": "", 
            "tag": 1, 
            "desc": " 自动下机机械手夹爪4气缸异常报警！"
        }, 
        "D2163": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event163"
        }, 
        "D2164": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event164"
        }, 
        "D2165": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event165"
        }, 
        "D2166": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event166"
        }, 
        "D2167": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event167"
        }, 
        "D2168": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event168"
        }, 
        "D2169": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event169"
        }, 
        "D2170": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event170"
        }, 
        "D2171": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event171"
        }, 
        "D2172": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event172"
        }, 
        "D2173": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event173"
        }, 
        "D2174": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道A升降机运转超时报警"
        }, 
        "D2175": {
            "alias": "", 
            "tag": 1, 
            "desc": " 轨道B升降机运转超时报警"
        }, 
        "D2176": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event176"
        }, 
        "D2177": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event177"
        }, 
        "D2178": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event178"
        }, 
        "D2179": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event179"
        }, 
        "D2180": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event180"
        }, 
        "D2181": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event181"
        }, 
        "D2182": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event182"
        }, 
        "D2183": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event183"
        }, 
        "D2184": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event184"
        }, 
        "D2185": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event185"
        }, 
        "D2186": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event186"
        }, 
        "D2187": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event187"
        }, 
        "D2188": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event188"
        }, 
        "D2189": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event189"
        }, 
        "D2190": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event190"
        }, 
        "D2191": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event191"
        }, 
        "D2192": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event192"
        }, 
        "D2193": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event193"
        }, 
        "D2194": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event194"
        }, 
        "D2195": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event195"
        }, 
        "D2196": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event196"
        }, 
        "D2197": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event197"
        }, 
        "D2198": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event198"
        }, 
        "D2199": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event199"
        }, 
        "D2200": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event200"
        }, 
        "D2201": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event201"
        }, 
        "D2202": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event202"
        }, 
        "D2203": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event203"
        }, 
        "D2204": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event204"
        }, 
        "D2205": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event205"
        }, 
        "D2206": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event206"
        }, 
        "D2207": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event207"
        }, 
        "D2208": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event208"
        }, 
        "D2209": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event209"
        }, 
        "D2210": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event210"
        }, 
        "D2211": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event211"
        }, 
        "D2212": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event212"
        }, 
        "D2213": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event213"
        }, 
        "D2214": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event214"
        }, 
        "D2215": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event215"
        }, 
        "D2216": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event216"
        }, 
        "D2217": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event217"
        }, 
        "D2218": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event218"
        }, 
        "D2219": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event219"
        }, 
        "D2220": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event220"
        }, 
        "D2221": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event221"
        }, 
        "D2222": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event222"
        }, 
        "D2223": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event223"
        }, 
        "D2224": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event224"
        }, 
        "D2225": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event225"
        }, 
        "D2226": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event226"
        }, 
        "D2227": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event227"
        }, 
        "D2228": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event228"
        }, 
        "D2229": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event229"
        }, 
        "D2230": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event230"
        }, 
        "D2231": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event231"
        }, 
        "D2232": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event232"
        }, 
        "D2233": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event233"
        }, 
        "D2234": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event234"
        }, 
        "D2235": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event235"
        }, 
        "D2236": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event236"
        }, 
        "D2237": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event237"
        }, 
        "D2238": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event238"
        }, 
        "D2239": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event239"
        }, 
        "D2240": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event240"
        }, 
        "D2241": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event241"
        }, 
        "D2242": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event242"
        }, 
        "D2243": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event243"
        }, 
        "D2244": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event244"
        }, 
        "D2245": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event245"
        }, 
        "D2246": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event246"
        }, 
        "D2247": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event247"
        }, 
        "D2248": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event248"
        }, 
        "D2249": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event249"
        }, 
        "D2250": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event250"
        }, 
        "D2251": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event251"
        }, 
        "D2252": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event252"
        }, 
        "D2253": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event253"
        }, 
        "D2254": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event254"
        }, 
        "D2255": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event255"
        }, 
        "D2256": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event256"
        }, 
        "D2257": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event257"
        }, 
        "D2258": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event258"
        }, 
        "D2259": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event259"
        }, 
        "D2260": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event260"
        }, 
        "D2261": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event261"
        }, 
        "D2262": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event262"
        }, 
        "D2263": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event263"
        }, 
        "D2264": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event264"
        }, 
        "D2265": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event265"
        }, 
        "D2266": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event266"
        }, 
        "D2267": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event267"
        }, 
        "D2268": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event268"
        }, 
        "D2269": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event269"
        }, 
        "D2270": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event270"
        }, 
        "D2271": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event271"
        }, 
        "D2272": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event272"
        }, 
        "D2273": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event273"
        }, 
        "D2274": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event274"
        }, 
        "D2275": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event275"
        }, 
        "D2276": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event276"
        }, 
        "D2277": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event277"
        }, 
        "D2278": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event278"
        }, 
        "D2279": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event279"
        }, 
        "D2280": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event280"
        }, 
        "D2281": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event281"
        }, 
        "D2282": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event282"
        }, 
        "D2283": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event283"
        }, 
        "D2284": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event284"
        }, 
        "D2285": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event285"
        }, 
        "D2286": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event286"
        }, 
        "D2287": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event287"
        }, 
        "D2288": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event288"
        }, 
        "D2289": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event289"
        }, 
        "D2290": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event290"
        }, 
        "D2291": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event291"
        }, 
        "D2292": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event292"
        }, 
        "D2293": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event293"
        }, 
        "D2294": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event294"
        }, 
        "D2295": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event295"
        }, 
        "D2296": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event296"
        }, 
        "D2297": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event297"
        }, 
        "D2298": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event298"
        }, 
        "D2299": {
            "alias": "", 
            "tag": 1, 
            "desc": " Event299"
        }
    }
}
