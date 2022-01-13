# -*- coding: utf-8 -*-

parameterHeaderSingle = ["time", "model", "fluxsolder", "fluxspeed", "fluxcnywidth", "spraylength", "spraywidth",
                    "nozzlespeed", "spraypress", "solderflow", "solderproportion", "wsspeed", "wscnywidth",
                    "PreheatZone1", "PreheatZone2", "PreheatZone3", "stp", "wave1motor", "wave2motor",
                    "wave1height", "wave2height", "cnyangle"]
parameterHeader = {
            ("D06", "MP18", "MP-TJ-ATM-116"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-016"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-GLU-005"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-017"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-WLD-052"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-ATM-064"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-018"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-GLU-006"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-019"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-020"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-099"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-100"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-101"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-102"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-103"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-GLU-041"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-CNY-021"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-GLU-042"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D06", "MP18", "MP-TJ-ATM-063"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"]
           }

errCodeLength = 16
errcodeDict = {
            ("D06", "MP18", "MP-TJ-ATM-116"): {
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
            ("D06", "MP18", "MP-TJ-GLU-005"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event52"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工段远程模块连接失败，请检查，后断电重启！！"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "当前机种编号与记忆机种不一致，请检查，及时调取或者保存参数"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event100"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X45 下限X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X62 下限X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X75 下限X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A产品检测异常"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B产品检测异常"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶前检测产品有浮高，请人工确认"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event116"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event117"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸上限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸下限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸报警，请检查IO 上限X220 下限X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸上限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸下限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸报警，请检查IO 上限X226 下限X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A步进马达运转超时"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B步进马达运转超时"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event129"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event132"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event133"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event135"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event136"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event137"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event138"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶1缺胶报警，请及时换胶！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶2缺胶报警，请及时换胶！"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶3缺胶报警，请及时换胶！"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶4缺胶报警，请及时换胶！"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event145"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸松开异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧感应X34X36，松开感应X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸夹紧异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开感应松开感应X50X52，夹紧感应X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸松开异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧感应X64X66，松开感应X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸夹紧异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开感应X80X82，夹紧感应X77X81"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event162"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event174"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event299"
                }
            }, 
            ("D06", "MP18", "MP-TJ-WLD-052"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 焊锡安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event52"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event65"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event66"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event71"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event100"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升气缸上升异常，请检查Y21、X31"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升气缸下降异常，请检查Y22、X32"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升气缸异常，请检查X31、X32"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升气缸上升异常，请检查Y25、X35"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升气缸下降异常，请检查Y26、X36"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升气缸异常，请检查X35、X36"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event107"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event108"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event109"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A到位阻挡下降超时"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B到位阻挡下降超时"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 烙铁头1到达最大使用次数，请更换"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 烙铁头2到达最大使用次数，请更换"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 机械手送锡步进1缺锡检测报警"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 机械手送锡步进1堵锡检测报警"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 机械手送锡步进2缺锡检测报警"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 机械手送锡步进2堵锡检测报警"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A压条限高异常报警，请检查压条是否装好！"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B压条限高异常报警，请检查压条是否装好！"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 烙铁寿命到达设定次数，请确认！"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 烙铁未打开报警，请确认！检查输出Y17是否有输出！_x000D_\n点击复位按键清除报警！"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event122"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event123"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event124"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event125"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event129"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-1-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-2-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-1-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-2-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-1-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-2-X-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置X位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-1-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-2-Y-位置与偏移位置间距大于1CM，_x000D_\n或者抬升完成位置Y位置间距大于1CM，_x000D_\n请重新确定焊点位置是否正确！"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-1-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A焊点-2-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-1-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B焊点-2-位置R1-R2角度差值大于30度，_x000D_\n请检查R轴角度是否正确！"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 焊锡机械手不在安全位置，X-Y的定位输出位置超出1.5CM,_x000D_\n请记录异常解除里相关信息，请复位设备，以及检查焊点位置是否准确！"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event150"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event151"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event152"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event153"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event154"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event155"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event156"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event157"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event158"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event159"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event160"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event161"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event162"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event174"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event299"
                }, 
                "MW2300": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event300"
                }
            }, 
            ("D06", "MP18", "MP-TJ-ATM-064"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event52"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event65"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event66"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event100"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位顶升气缸上升异常，请查看输入“X32”或输出“Y32”"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位顶升气缸下降异常，请查看输入“X33”或输出“Y33”"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位顶升气缸感应异常，请查看输入“X32”或“X33”"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位定位气缸伸出异常，请查看输入“X34 X36”或输出“Y34”"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位定位气缸退回异常，请查看输入“X35 X37”或输出“Y35”"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位定位气缸异常，请查看输入“X35 X37 X34 X36”"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位下机芯位治具旋转气缸旋转异常，请查看输入“X40 X42”或输出“Y36”"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位下机芯位治具旋转气缸复位异常，请查看输入“X41 X43”或输出“Y37”"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A下机芯位下机芯位治具旋转气缸异常，请查看输入“X41 X42 X43 X40”"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A放行超时，请检查是否卡治具！"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位顶升气缸上升异常，请查看输入“X45”或输出“Y41”"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位顶升气缸下降异常，请查看输入“X46”或输出“Y42”"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位顶升气缸感应异常，请查看输入“X45”或“X46”"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位定位气缸伸出异常，请查看输入“X47 X51”或输出“Y43”"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位定位气缸退回异常，请查看输入“X50 X52”或输出“Y44”"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位定位气缸异常，请查看输入“X47 X50 X51 X52”"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位下机芯位治具旋转气缸旋转异常，请查看输入“X53 X55”或输出“Y45”"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位下机芯位治具旋转气缸复位异常，请查看输入“X54 X56”或输出“Y46”"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B下机芯位下机芯位治具旋转气缸异常，请查看输入“X53 X54 X55 X56”"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event121"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event122"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event123"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event124"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件上下气缸上升异常，请查看输入“X71 X73”或输出“Y55”"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件上下气缸下降异常，请查看输入“X70 X72”或输出“Y54”"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件上下气缸异常，请查看输入“X70 X71 X72 X73”"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件夹爪气缸松开异常，请查看输入“X74 X75”或输出“Y57”"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件夹爪气缸夹紧异常，请查看输入“X74 X75”或输出“Y56”"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹压件夹爪气缸异常，请查看输入“X74 X75”"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹PCB夹爪气缸松开异常，请查看输入“X76 X77”或输出“Y61”"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹PCB夹爪气缸夹紧异常，请查看输入“X76 X77”或输出“Y60”"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A机械手夹PCB夹爪气缸异常，请查看输入“X76 X77”"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B放行超时，请检查是否卡治具！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件上下气缸上升异常，请查看输入“X81 X83”或输出“Y65”"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件上下气缸下降异常，请查看输入“X80 X82”或输出“Y64”"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件上下气缸异常，请查看输入“X80 X81 X82 X83”"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件夹爪气缸松开异常，请查看输入“X84 X85”或输出“Y67”"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件夹爪气缸夹紧异常，请查看输入“X84 X85”或输出“Y66”"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹压件夹爪气缸异常，请查看输入“X84 X85”"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹PCB夹爪气缸松开异常，请查看输入“X86 X87”或输出“Y71”"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹PCB夹爪气缸夹紧异常，请查看输入“X86 X87”或输出“Y80”"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B机械手夹PCB夹爪气缸异常，请查看输入“X86 X87”"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event150"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event299"
                }
            }, 
            ("D06", "MP18", "MP-TJ-GLU-006"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event52"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工段远程模块连接失败，请检查，后断电重启！！"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "当前机种编号与记忆机种不一致，请检查，及时调取或者保存参数"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event100"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X45 下限X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X62 下限X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X75 下限X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A产品检测异常"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B产品检测异常"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶前检测产品有浮高，请人工确认"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event116"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event117"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸上限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸下限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸报警，请检查IO 上限X220 下限X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸上限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸下限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸报警，请检查IO 上限X226 下限X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A步进马达运转超时"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B步进马达运转超时"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event129"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event132"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event133"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event135"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event136"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event137"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event138"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶1缺胶报警，请及时换胶！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶2缺胶报警，请及时换胶！"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶3缺胶报警，请及时换胶！"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶4缺胶报警，请及时换胶！"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event145"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸松开异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧感应X34X36，松开感应X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸夹紧异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开感应松开感应X50X52，夹紧感应X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸松开异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧感应X64X66，松开感应X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸夹紧异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开感应X80X82，夹紧感应X77X81"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event162"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event174"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event299"
                }
            }, 
            ("D06", "MP18", "MP-TJ-GLU-041"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工段远程模块连接失败，请检查，后断电重启！！"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "当前机种编号与记忆机种不一致，请检查，及时调取或者保存参数"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "伺服在线失败，请检查！"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X45 下限X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X62 下限X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X75 下限X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A产品检测异常"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B产品检测异常"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶前检测产品有浮高，请人工确认"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event116"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event117"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸上限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸下限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸报警，请检查IO 上限X220 下限X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸上限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸下限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸报警，请检查IO 上限X226 下限X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A步进马达运转超时"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B步进马达运转超时"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event129"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event132"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event133"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event135"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event136"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event137"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event138"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶1缺胶检测报警，请及时换胶！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶2缺胶检测报警，请及时换胶！"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶3缺胶检测报警，请及时换胶！"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶4缺胶检测报警，请及时换胶！"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event145"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸松开异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧感应X34X36，松开感应X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸夹紧异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开感应松开感应X50X52，夹紧感应X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸松开异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧感应X64X66，松开感应X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸夹紧异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开感应X80X82，夹紧感应X77X81"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event162"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event174"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event299"
                }
            }, 
            ("D06", "MP18", "MP-TJ-GLU-042"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶工位安全门打开_x000D_\n请人工确认"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工段远程模块连接失败，请检查，后断电重启！！"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "当前机种编号与记忆机种不一致，请检查，及时调取或者保存参数"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "伺服在线失败，请检查！"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y32 下降Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X45 下限X46 上升Y41 下降Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X45 下限X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X62 下限X63 上升Y61 下降Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X62 下限X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X75 下限X76 上升Y70 下降Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X75 下限X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A产品检测异常"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B产品检测异常"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶前检测产品有浮高，请人工确认"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event116"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event117"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸上限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸下限报警，请检查IO 上限X220 下限X221 上升Y220 下降Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A升降机气缸报警，请检查IO 上限X220 下限X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸上限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸下限报警，请检查IO 上限X226 下限X227 上升Y226 下降Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B升降机气缸报警，请检查IO 上限X226 下限X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道A步进马达运转超时"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "人工位轨道B步进马达运转超时"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event126"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event127"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event128"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event129"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道A入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "轨道B入口升降机平台马达运转超时_x000D_\n请人工检查是否卡治具，点动复位按钮继续"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event132"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event133"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event135"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event136"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event137"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event138"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶1缺胶检测报警，请及时换胶！"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶2缺胶检测报警，请及时换胶！"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶3缺胶检测报警，请及时换胶！"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "胶桶4缺胶检测报警，请及时换胶！"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event145"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸松开异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧异常，夹紧感应X34X36，松开感应X35X37，松开Y35夹紧Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道A定位气缸夹紧感应X34X36，松开感应X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸夹紧异常，松开感应X50X52，夹紧感应X47X51，松开Y35夹紧Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶1轨道B定位气缸松开感应松开感应X50X52，夹紧感应X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸松开异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧异常，夹紧感应X64X66，松开感应X65X67，松开Y64夹紧Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道A定位气缸夹紧感应X64X66，松开感应X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸夹紧异常，松开感应X80X82，夹紧感应X77X81，松开Y73夹紧Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "点胶2轨道B定位气缸松开感应X80X82，夹紧感应X77X81"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event162"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event174"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event175"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "Event299"
                }
            }, 
            ("D06", "MP18", "MP-TJ-ATM-063"): {
                "MW2000": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event0"
                }, 
                "MW2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event1"
                }, 
                "MW2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event2"
                }, 
                "MW2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event3"
                }, 
                "MW2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event4"
                }, 
                "MW2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event5"
                }, 
                "MW2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event6"
                }, 
                "MW2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event7"
                }, 
                "MW2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event8"
                }, 
                "MW2009": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event9"
                }, 
                "MW2010": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event10"
                }, 
                "MW2011": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event11"
                }, 
                "MW2012": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event12"
                }, 
                "MW2013": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event13"
                }, 
                "MW2014": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event14"
                }, 
                "MW2015": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event15"
                }, 
                "MW2016": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event16"
                }, 
                "MW2017": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event17"
                }, 
                "MW2018": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event18"
                }, 
                "MW2019": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event19"
                }, 
                "MW2020": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event20"
                }, 
                "MW2021": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event21"
                }, 
                "MW2022": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event22"
                }, 
                "MW2023": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event23"
                }, 
                "MW2024": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event24"
                }, 
                "MW2025": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event25"
                }, 
                "MW2026": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event26"
                }, 
                "MW2027": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event27"
                }, 
                "MW2028": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event28"
                }, 
                "MW2029": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event29"
                }, 
                "MW2030": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event30"
                }, 
                "MW2031": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event31"
                }, 
                "MW2032": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event32"
                }, 
                "MW2033": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event33"
                }, 
                "MW2034": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event34"
                }, 
                "MW2035": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event35"
                }, 
                "MW2036": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event36"
                }, 
                "MW2037": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event37"
                }, 
                "MW2038": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event38"
                }, 
                "MW2039": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event39"
                }, 
                "MW2040": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event40"
                }, 
                "MW2041": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event41"
                }, 
                "MW2042": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event42"
                }, 
                "MW2043": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event43"
                }, 
                "MW2044": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event44"
                }, 
                "MW2045": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event45"
                }, 
                "MW2046": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event46"
                }, 
                "MW2047": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event47"
                }, 
                "MW2048": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event48"
                }, 
                "MW2049": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event49"
                }, 
                "MW2050": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event52"
                }, 
                "MW2053": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event53"
                }, 
                "MW2054": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event54"
                }, 
                "MW2055": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event55"
                }, 
                "MW2056": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event56"
                }, 
                "MW2057": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与上一台PLC通讯异常，请检查网络连接_x000D_\n如没有上一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用上一台PLC连接异常报警"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与下一台PLC通讯异常，请检查网络连接_x000D_\n如没有下一台PLC，则在数据设置画面-功能参数设定里面_x000D_\n禁用下一台PLC连接异常报警"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 与PC通讯异常，请检查网络连接_x000D_\n如没有PC，则在数据设置画面-功能参数设定里面_x000D_\n禁用PC连接异常报警"
                }, 
                "MW2060": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event60"
                }, 
                "MW2061": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event61"
                }, 
                "MW2062": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event62"
                }, 
                "MW2063": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event63"
                }, 
                "MW2064": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event64"
                }, 
                "MW2065": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event65"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event66"
                }, 
                "MW2067": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event67"
                }, 
                "MW2068": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event68"
                }, 
                "MW2069": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event69"
                }, 
                "MW2070": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event70"
                }, 
                "MW2071": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 设备伺服报警，请检查伺服驱动器的报错代码"
                }, 
                "MW2072": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event72"
                }, 
                "MW2073": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event73"
                }, 
                "MW2074": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event74"
                }, 
                "MW2075": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event75"
                }, 
                "MW2076": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event76"
                }, 
                "MW2077": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event77"
                }, 
                "MW2078": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event78"
                }, 
                "MW2079": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event79"
                }, 
                "MW2080": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event80"
                }, 
                "MW2081": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event81"
                }, 
                "MW2082": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event82"
                }, 
                "MW2083": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event83"
                }, 
                "MW2084": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event84"
                }, 
                "MW2085": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event85"
                }, 
                "MW2086": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event86"
                }, 
                "MW2087": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event87"
                }, 
                "MW2088": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event88"
                }, 
                "MW2089": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event89"
                }, 
                "MW2090": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event90"
                }, 
                "MW2091": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event91"
                }, 
                "MW2092": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event92"
                }, 
                "MW2093": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event93"
                }, 
                "MW2094": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event94"
                }, 
                "MW2095": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event95"
                }, 
                "MW2096": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event96"
                }, 
                "MW2097": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event97"
                }, 
                "MW2098": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event98"
                }, 
                "MW2099": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event99"
                }, 
                "MW2100": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event100"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A升降机上升异常，请检查“X30”或“Y20”，按复位消除报警"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A升降机下降异常，请检查“X31”或“Y21”，按复位消除报警"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A升降机气缸异常报警！请查看X30 X31"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升定位气缸上升异常，请检查“X34”或“Y24”，按复位消除报警"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升定位气缸下降异常，请检查“X35”或“Y25”，按复位消除报警"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A顶升气缸异常报警！请查看X34 X35"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A定位气缸伸出异常，请检查“X36 X40 ” 或“Y26”，按复位消除报警"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A定位气缸退回异常，请检查“X37 X41”或“Y27”，按复位消除报警"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A定位气缸异常报警！！！请查看“X36 X37 X40 X41”"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A旋转气缸旋转异常，请检查“X42 X44”或“Y30”，按复位消除报警"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A旋转气缸复位异常，请检查“X43 X45”或“Y31”，按复位消除报警"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A旋转气缸异常报警！请查看 X42 X43 X44 X45"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event113"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event114"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event115"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event116"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event117"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event118"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event119"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event120"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B升降机上升异常，请检查“X50”或“Y34”，按复位消除报警"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B升降机下降异常，请检查“X51”或“Y35”，按复位消除报警"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B升降机气缸异常报警！请查看X50 X51"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升定位气缸上升异常，请检查“X54”或“Y40”，按复位消除报警"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升定位气缸下降异常，请检查“X55”或“Y41”，按复位消除报警"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B顶升气缸异常报警！请查看X54 X55"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B定位气缸伸出异常，请检查“X56 X60 ” 或“Y42”，按复位消除报警"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B定位气缸退回异常，请检查“X57 X61”或“Y43”，按复位消除报警"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B定位气缸异常报警！！！请查看“X56 X57 X60 X61”"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B旋转气缸旋转异常，请检查“X62 X64”或“Y44”，按复位消除报警"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B旋转气缸复位异常，请检查“X63 X65”或“Y45”，按复位消除报警"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B旋转气缸异常报警！请查看 X62 X63 X64 X65"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event133"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event135"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event136"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event137"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event138"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event140"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event141"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event142"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event143"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event145"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event146"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event147"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event148"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event149"
                }, 
                "MW2150": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event150"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪1松开异常，请检查“X61”或“Y60”，按复位消除报警！"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪1夹紧异常，请检查“X61”或“Y60”，按复位消除报警！"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪1气缸异常报警！"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪2松开异常，请检查“X62”或“Y62”，按复位消除报警！"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪2夹紧异常，请检查“X62”或“Y62”，按复位消除报警！"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪2气缸异常报警！"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪3松开异常，请检查“X65”或“Y65”，按复位消除报警！"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪3夹紧异常，请检查“X65”或“Y64”，按复位消除报警！"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪3气缸异常报警！"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪4松开异常，请检查“X67”或“Y67”，按复位消除报警！"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪4夹紧异常，请检查“X67”或“Y66”，按复位消除报警！"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 自动下机机械手夹爪4气缸异常报警！"
                }, 
                "MW2163": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event163"
                }, 
                "MW2164": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event164"
                }, 
                "MW2165": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event165"
                }, 
                "MW2166": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event166"
                }, 
                "MW2167": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event167"
                }, 
                "MW2168": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event168"
                }, 
                "MW2169": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event169"
                }, 
                "MW2170": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event170"
                }, 
                "MW2171": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event171"
                }, 
                "MW2172": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event172"
                }, 
                "MW2173": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event173"
                }, 
                "MW2174": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道A升降机运转超时报警"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " 轨道B升降机运转超时报警"
                }, 
                "MW2176": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event176"
                }, 
                "MW2177": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event177"
                }, 
                "MW2178": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event178"
                }, 
                "MW2179": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event179"
                }, 
                "MW2180": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event180"
                }, 
                "MW2181": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event181"
                }, 
                "MW2182": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event182"
                }, 
                "MW2183": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event183"
                }, 
                "MW2184": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event184"
                }, 
                "MW2185": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event185"
                }, 
                "MW2186": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event186"
                }, 
                "MW2187": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event187"
                }, 
                "MW2188": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event188"
                }, 
                "MW2189": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event189"
                }, 
                "MW2190": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event190"
                }, 
                "MW2191": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event191"
                }, 
                "MW2192": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event192"
                }, 
                "MW2193": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event193"
                }, 
                "MW2194": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event194"
                }, 
                "MW2195": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event195"
                }, 
                "MW2196": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event196"
                }, 
                "MW2197": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event197"
                }, 
                "MW2198": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event198"
                }, 
                "MW2199": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event199"
                }, 
                "MW2200": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event200"
                }, 
                "MW2201": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event201"
                }, 
                "MW2202": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event202"
                }, 
                "MW2203": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event203"
                }, 
                "MW2204": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event204"
                }, 
                "MW2205": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event205"
                }, 
                "MW2206": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event206"
                }, 
                "MW2207": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event207"
                }, 
                "MW2208": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event208"
                }, 
                "MW2209": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event209"
                }, 
                "MW2210": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event210"
                }, 
                "MW2211": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event211"
                }, 
                "MW2212": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event212"
                }, 
                "MW2213": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event213"
                }, 
                "MW2214": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event214"
                }, 
                "MW2215": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event215"
                }, 
                "MW2216": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event216"
                }, 
                "MW2217": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event217"
                }, 
                "MW2218": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event218"
                }, 
                "MW2219": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event219"
                }, 
                "MW2220": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event220"
                }, 
                "MW2221": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event221"
                }, 
                "MW2222": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event222"
                }, 
                "MW2223": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event223"
                }, 
                "MW2224": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event224"
                }, 
                "MW2225": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event225"
                }, 
                "MW2226": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event226"
                }, 
                "MW2227": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event227"
                }, 
                "MW2228": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event228"
                }, 
                "MW2229": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event229"
                }, 
                "MW2230": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event230"
                }, 
                "MW2231": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event231"
                }, 
                "MW2232": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event232"
                }, 
                "MW2233": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event233"
                }, 
                "MW2234": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event234"
                }, 
                "MW2235": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event235"
                }, 
                "MW2236": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event236"
                }, 
                "MW2237": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event237"
                }, 
                "MW2238": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event238"
                }, 
                "MW2239": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event239"
                }, 
                "MW2240": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event240"
                }, 
                "MW2241": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event241"
                }, 
                "MW2242": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event242"
                }, 
                "MW2243": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event243"
                }, 
                "MW2244": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event244"
                }, 
                "MW2245": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event245"
                }, 
                "MW2246": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event246"
                }, 
                "MW2247": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event247"
                }, 
                "MW2248": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event248"
                }, 
                "MW2249": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event249"
                }, 
                "MW2250": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event250"
                }, 
                "MW2251": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event251"
                }, 
                "MW2252": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event252"
                }, 
                "MW2253": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event253"
                }, 
                "MW2254": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event254"
                }, 
                "MW2255": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event255"
                }, 
                "MW2256": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event256"
                }, 
                "MW2257": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event257"
                }, 
                "MW2258": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event258"
                }, 
                "MW2259": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event259"
                }, 
                "MW2260": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event260"
                }, 
                "MW2261": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event261"
                }, 
                "MW2262": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event262"
                }, 
                "MW2263": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event263"
                }, 
                "MW2264": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event264"
                }, 
                "MW2265": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event265"
                }, 
                "MW2266": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event266"
                }, 
                "MW2267": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event267"
                }, 
                "MW2268": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event268"
                }, 
                "MW2269": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event269"
                }, 
                "MW2270": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event270"
                }, 
                "MW2271": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event271"
                }, 
                "MW2272": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event272"
                }, 
                "MW2273": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event273"
                }, 
                "MW2274": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event274"
                }, 
                "MW2275": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event275"
                }, 
                "MW2276": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event276"
                }, 
                "MW2277": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event277"
                }, 
                "MW2278": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event278"
                }, 
                "MW2279": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event279"
                }, 
                "MW2280": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event280"
                }, 
                "MW2281": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event281"
                }, 
                "MW2282": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event282"
                }, 
                "MW2283": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event283"
                }, 
                "MW2284": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event284"
                }, 
                "MW2285": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event285"
                }, 
                "MW2286": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event286"
                }, 
                "MW2287": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event287"
                }, 
                "MW2288": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event288"
                }, 
                "MW2289": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event289"
                }, 
                "MW2290": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event290"
                }, 
                "MW2291": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event291"
                }, 
                "MW2292": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event292"
                }, 
                "MW2293": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event293"
                }, 
                "MW2294": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event294"
                }, 
                "MW2295": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event295"
                }, 
                "MW2296": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event296"
                }, 
                "MW2297": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event297"
                }, 
                "MW2298": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event298"
                }, 
                "MW2299": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event299"
                }
            },
            ("D06", "MP18", "MP-TJ-CNY-016"):{},
            ("D06", "MP18", "MP-TJ-CNY-017"):{},
            ("D06", "MP18", "MP-TJ-CNY-018"):{},
            ("D06", "MP18", "MP-TJ-CNY-019"):{},
            ("D06", "MP18", "MP-TJ-CNY-020"):{},
            ("D06", "MP18", "MP-TJ-CNY-099"):{},
            ("D06", "MP18", "MP-TJ-CNY-100"):{},
            ("D06", "MP18", "MP-TJ-CNY-101"):{},
            ("D06", "MP18", "MP-TJ-CNY-102"):{},
            ("D06", "MP18", "MP-TJ-CNY-103"):{},
            ("D06", "MP18", "MP-TJ-CNY-021"):{}
}
