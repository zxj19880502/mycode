# -*- coding: utf-8 -*-

parameterHeaderSingle = ["time", "model", "fluxsolder", "fluxspeed", "fluxcnywidth", "spraylength", "spraywidth",
                    "nozzlespeed", "spraypress", "solderflow", "solderproportion", "wsspeed", "wscnywidth",
                    "PreheatZone1", "PreheatZone2", "PreheatZone3", "stp", "wave1motor", "wave2motor",
                    "wave1height", "wave2height", "cnyangle"]
parameterHeader = {
            ("D05", "MP18", "MP-TJ-ATM-060"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-CNY-094"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-CNY-098"):["DateTime","DeviceSn","Count","WorkMode","Status","ErrorCode"],            
            ("D05", "MP18", "MP-TJ-GLU-039"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-CCD-004"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-ACA-001"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],            
            ("D05", "MP18", "MP-TJ-ABL-007"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-GLU-040"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-MAP-021"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],            
            ("D05", "MP18", "MP-TJ-APA-001"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-ATM-131"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-ACA-002"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-CCD-003"):["DateTime","DeviceSn","Count","Speed","Status","ErrorCode"],
            ("D05", "MP18", "MP-TJ-ATM-061"):["DateTime","DeviceSn","Count","Pass","Fail","Speed","Status","ErrorCode"]                 
           }

errCodeLength = 16
errcodeDict = {
                ("D05", "MP18", "MP-TJ-ATM-131"): {
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
                        "desc": " 启动条件不足,请确认平移伺服有无复位,轨道顶升气缸下限是否_x000D_\n到位."
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 轨道A超声波顶升气缸1下降异常，请检查Y32、X32"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波顶升气缸1上升异常，请检查Y33、X33"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波顶升气缸1异常，请检查X32、X33"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波顶升气缸2下降异常，请检查Y34、X34"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波顶升气缸2上升异常，请检查Y35、X35"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波顶升气缸2异常，请检查X34、X35"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手旋转气缸正转异常，请检查Y44、X44"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手旋转气缸反转异常，请检查Y45、X45"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手旋转气缸异常，请检查X44、X45"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手上下气缸上升异常，请检查Y46、X46"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手上下气缸下降异常，请检查Y47、X47"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手上下气缸异常，请检查X46、X47"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波铆合升降气缸上升异常，请检查Y50、X50"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波铆合升降气缸下降异常，请检查Y51、X51"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波铆合升降气缸异常，请检查X50、X51"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波铆合定位气缸伸出异常，请检查Y52、X52"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波铆合定位气缸退回异常，请检查Y52、X53"
                    }, 
                    "MW2118": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event118"
                    }, 
                    "MW2119": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波卷膜机构上升异常，请检查Y54、X54"
                    }, 
                    "MW2120": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波卷膜机构下降异常，请检查Y55、X55"
                    }, 
                    "MW2121": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波卷膜机构异常，请检查X54、X55"
                    }, 
                    "MW2122": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1松开异常，请检查Y40、X41"
                    }, 
                    "MW2123": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1夹紧异常，请检查Y41、X41"
                    }, 
                    "MW2124": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event124"
                    }, 
                    "MW2125": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2松开异常，请检查Y42、X43"
                    }, 
                    "MW2126": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2夹紧异常，请检查Y43、X43"
                    }, 
                    "MW2127": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event127"
                    }, 
                    "MW2128": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1松开异常，请检查Y40、X40"
                    }, 
                    "MW2129": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1夹紧异常，请检查Y41、X40"
                    }, 
                    "MW2130": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1松开异常，请检查Y40、X41"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪1夹紧异常，请检查Y41、X41"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event133"
                    }, 
                    "MW2134": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2松开异常，请检查Y42、X43"
                    }, 
                    "MW2135": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2夹紧异常，请检查Y43、X43"
                    }, 
                    "MW2136": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event136"
                    }, 
                    "MW2137": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2松开异常，请检查Y42、X42"
                    }, 
                    "MW2138": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波机械手夹爪2夹紧异常，请检查Y43、X42"
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
                        "desc": " 轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A治具ID读取失败"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A治具ID读取超时"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A治具到位阻挡下降超时"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A铆合位记忆有产品实际检测无产品"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波_调试选择开关错误"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波触发超时"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A卷膜机构薄膜缺料"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A治具绑定取失败"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A超声波超时，无铆合PC-触发信号"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A铆合位条码发送超时/失败报警！请检查超声波软件是否打开？_x000D_\n点击复位清除报警！！"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A铆合位条码发送重复报警！请检查超声波软件是否打开？_x000D_\n点击复位清除报警！请确认产品条码！"
                    }, 
                    "MW2162": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B铆合位条码发送超时/失败报警！请检查超声波软件是否打开？_x000D_\n点击复位清除报警！重复触发！"
                    }, 
                    "MW2163": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B铆合位条码发送重复报警！请检查超声波软件是否打开？_x000D_\n点击复位清除报警！请确认产品条码！"
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
                        "desc": " 轨道A扫条码超时，请在异常解除里选择跳过！"
                    }, 
                    "MW2171": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B扫条码超时，请在异常解除里选择跳过！"
                    }, 
                    "MW2172": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A铆合位置产品没有铆合完成标记，也无扫码完成信号，_x000D_\n请把产品拿走，或者在异常解除中，_x000D_\n选择将产品标记为已铆合！"
                    }, 
                    "MW2173": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B铆合位置产品没有铆合完成标记，也无扫码完成信号，_x000D_\n请把产品拿走，或者在异常解除中，_x000D_\n选择将产品标记为已铆合！"
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
                        "desc": " 轨道B超声波顶升气缸1下降异常，请检查Y202、X202"
                    }, 
                    "MW2202": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波顶升气缸1上升异常，请检查Y203、X203"
                    }, 
                    "MW2203": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波顶升气缸1异常，请检查X202、X203"
                    }, 
                    "MW2204": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波顶升气缸2下降异常，请检查Y204、X204"
                    }, 
                    "MW2205": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波顶升气缸2上升异常，请检查Y205、X205"
                    }, 
                    "MW2206": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波顶升气缸2异常，请检查X204、X205"
                    }, 
                    "MW2207": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手旋转气缸正转异常，请检查Y214、X214"
                    }, 
                    "MW2208": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手旋转气缸反转异常，请检查Y215、X215"
                    }, 
                    "MW2209": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手旋转气缸异常，请检查X214、X215"
                    }, 
                    "MW2210": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手上下气缸上升异常，请检查Y216、X216"
                    }, 
                    "MW2211": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手上下气缸下降异常，请检查Y217、X217"
                    }, 
                    "MW2212": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手上下气缸异常，请检查X216、X217"
                    }, 
                    "MW2213": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波铆合升降气缸上升异常，请检查Y220、X220"
                    }, 
                    "MW2214": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波铆合升降气缸下降异常，请检查Y221、X221"
                    }, 
                    "MW2215": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波铆合升降气缸异常，请检查X220、X221"
                    }, 
                    "MW2216": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波铆合定位气缸伸出异常，请检查Y222、X222"
                    }, 
                    "MW2217": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波铆合定位气缸退回异常，请检查Y222、X223"
                    }, 
                    "MW2218": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event218"
                    }, 
                    "MW2219": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波卷膜机构上升异常，请检查Y224、X224"
                    }, 
                    "MW2220": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波卷膜机构下降异常，请检查Y225、X225"
                    }, 
                    "MW2221": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波卷膜机构异常，请检查X224、X225"
                    }, 
                    "MW2222": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1松开异常，请检查Y210、X211"
                    }, 
                    "MW2223": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1夹紧异常，请检查Y211、X211"
                    }, 
                    "MW2224": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event224"
                    }, 
                    "MW2225": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2松开异常，请检查Y212、X213"
                    }, 
                    "MW2226": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2夹紧异常，请检查Y213、X213"
                    }, 
                    "MW2227": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event227"
                    }, 
                    "MW2228": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1松开异常，请检查Y210、X210"
                    }, 
                    "MW2229": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1夹紧异常，请检查Y211、X210"
                    }, 
                    "MW2230": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event230"
                    }, 
                    "MW2231": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1松开异常，请检查Y210、X211"
                    }, 
                    "MW2232": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪1夹紧异常，请检查Y211、X211"
                    }, 
                    "MW2233": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event233"
                    }, 
                    "MW2234": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2松开异常，请检查Y212、X213"
                    }, 
                    "MW2235": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2夹紧异常，请检查Y213、X213"
                    }, 
                    "MW2236": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event236"
                    }, 
                    "MW2237": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2松开异常，请检查Y212、X212"
                    }, 
                    "MW2238": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波机械手夹爪2夹紧异常，请检查Y213、X212"
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
                        "desc": " 轨道B后缓冲阻挡下降超时"
                    }, 
                    "MW2251": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B治具ID读取失败"
                    }, 
                    "MW2252": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B治具ID读取超时"
                    }, 
                    "MW2253": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B治具到位阻挡下降超时"
                    }, 
                    "MW2254": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B铆合位记忆有产品实际检测无产品"
                    }, 
                    "MW2255": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波_调试选择开关错误"
                    }, 
                    "MW2256": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波触发超时"
                    }, 
                    "MW2257": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B卷膜机构薄膜缺料"
                    }, 
                    "MW2258": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B治具绑定取失败"
                    }, 
                    "MW2259": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B超声波超时，无铆合PC-触发信号"
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
                ("D05", "MP18", "MP-TJ-ATM-060"): {
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
                        "desc": "点胶位安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2052": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "升降机安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2053": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "上机人工位1 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2054": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "上机人工位2 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2055": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event55"
                    }, 
                    "MW2056": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "系统网线总成断开，请检查设备远程扩展设备的网线连接!"
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
                        "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X36 下限X37 上升Y26 下降Y27"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X36 下限X37 上升Y26 下降Y27"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X32 下限X33"
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
                        "desc": "轨道B点胶前检测产品有浮高，请人工确认，点动复位清除！"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶前检测产品有浮高，请人工确认，点动复位清除！"
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
                        "desc": "胶桶1缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶2缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶3缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2143": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶4缺胶检测报警，请及时更换胶桶！"
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
                        "desc": "Event150"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event151"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event152"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event153"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event154"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event155"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event156"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event157"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event158"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event159"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event160"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event161"
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
                ("D05", "MP18", "MP-TJ-GLU-039"): {
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
                        "desc": "点胶位安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2052": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "升降机安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2053": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "上机人工位1 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2054": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "上机人工位2 紧急停止按下，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2055": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event55"
                    }, 
                    "MW2056": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "系统网线总成断开，请检查设备远程扩展设备的网线连接!"
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
                        "desc": "轨道A点胶1顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸上限报警，请检查IO 上限X36 下限X37 上升Y26 下降Y27"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶1顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸上限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶2顶升气缸报警，请检查IO 上限X32 下限X33"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸上限报警，请检查IO 上限X36 下限X37 上升Y26 下降Y27"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸下限报警，请检查IO 上限X32 下限X33 上升Y22 下降Y23"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道B点胶2顶升气缸报警，请检查IO 上限X32 下限X33"
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
                        "desc": "轨道B点胶前检测产品有浮高，请人工确认，点动复位清除！"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "轨道A点胶前检测产品有浮高，请人工确认，点动复位清除！"
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
                        "desc": "胶桶1缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶2缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶3缺胶检测报警，请及时更换胶桶！"
                    }, 
                    "MW2143": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "胶桶4缺胶检测报警，请及时更换胶桶！"
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
                        "desc": "Event150"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event151"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event152"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event153"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event154"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event155"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event156"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event157"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event158"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event159"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event160"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event161"
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
                ("D05", "MP18", "MP-TJ-MAP-021"): {
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
                        "desc": " 工位1安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2052": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2053": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 返治具升降机安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 工位-1-轨道A读卡超时！"
                    }, 
                    "MW2086": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-1-轨道B读卡超时！"
                    }, 
                    "MW2087": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-2-轨道A读卡超时！"
                    }, 
                    "MW2088": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-2-轨道B读卡超时！"
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
                        "desc": " 工位1副轨道A顶升气缸上升异常，请检查X31,Y31"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A顶升气缸下降异常，请检查X32,Y32"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A顶升气缸异常，请检查X31,X32"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸上升异常，请检查X34,Y34"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸下降异常，请检查X35,Y35"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸异常，请检查X34,X35"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸上升异常，请检查X41,Y41"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸下降异常，请检查X42,Y42"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸异常，请检查X41,X42"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1松开异常，请检查X43、Y43"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1夹紧异常，请检查X44、Y44"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1异常，请检查X43、X44"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2松开异常，请检查X45、Y43"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2夹紧异常，请检查X46、Y44"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2异常，请检查X45、X46"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸上升异常，请检查X51,Y51"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸下降异常，请检查X52,Y52"
                    }, 
                    "MW2118": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸异常，请检查X51,X52"
                    }, 
                    "MW2119": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1松开异常，请检查X53、Y53"
                    }, 
                    "MW2120": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1夹紧异常，请检查X54、Y54"
                    }, 
                    "MW2121": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1异常，请检查X53、X54"
                    }, 
                    "MW2122": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2松开异常，请检查X55、Y53"
                    }, 
                    "MW2123": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2夹紧异常，请检查X56、Y54"
                    }, 
                    "MW2124": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2异常，请检查X55、X56"
                    }, 
                    "MW2125": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1上升异常，请检查X60、Y60"
                    }, 
                    "MW2126": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1下降异常，请检查X61、Y61"
                    }, 
                    "MW2127": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1异常，请检查X60、X61"
                    }, 
                    "MW2128": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪1松开异常，请检查X62、Y62"
                    }, 
                    "MW2129": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪1夹紧异常，请检查X62、Y63"
                    }, 
                    "MW2130": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1原点异常，请检查X64、Y64"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1动点异常，请检查X65、Y65"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1异常，请检查X64、X65"
                    }, 
                    "MW2134": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2上升异常，请检查X70、Y70"
                    }, 
                    "MW2135": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2下降异常，请检查X71、Y71"
                    }, 
                    "MW2136": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2异常，请检查X70、X71"
                    }, 
                    "MW2137": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪2松开异常，请检查X72、Y72"
                    }, 
                    "MW2138": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪2夹紧异常，请检查X72、Y73"
                    }, 
                    "MW2139": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event139"
                    }, 
                    "MW2140": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2原点异常，请检查X74、Y74"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2动点异常，请检查X75、Y75"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2异常，请检查X74、X75"
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
                        "desc": " 工位1主轨道A有产品条码为空报警"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A治具ID读取失败报警"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A治具ID读取超时报警"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B有产品条码为空报警"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B治具ID读取失败报警"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B治具ID读取超时报警"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A上下气缸1压PCBA异常报警"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A上下气缸2压PCBA异常报警"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B上下气缸1压PCBA异常报警"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B上下气缸2压PCBA异常报警"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A产品2扫条码失败报警"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A产品4扫条码失败报警"
                    }, 
                    "MW2162": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B产品2扫条码失败报警"
                    }, 
                    "MW2163": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B产品4扫条码失败报警"
                    }, 
                    "MW2164": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1副轨道A到位阻挡下降超时"
                    }, 
                    "MW2165": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1副轨道B到位阻挡下降超时"
                    }, 
                    "MW2166": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2167": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2168": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道A到位阻挡下降超时"
                    }, 
                    "MW2169": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道B到位阻挡下降超时"
                    }, 
                    "MW2170": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2171": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2172": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道A到位阻挡下降超时"
                    }, 
                    "MW2173": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道B到位阻挡下降超时"
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
                        "desc": " 工位2副轨道A顶升气缸上升异常，请检查X201,Y201"
                    }, 
                    "MW2202": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A顶升气缸下降异常，请检查X202,Y202"
                    }, 
                    "MW2203": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A顶升气缸异常，请检查X201,X202"
                    }, 
                    "MW2204": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸上升异常，请检查X204,Y204"
                    }, 
                    "MW2205": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸下降异常，请检查X205,Y205"
                    }, 
                    "MW2206": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸异常，请检查X204,X205"
                    }, 
                    "MW2207": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸上升异常，请检查X211,Y211"
                    }, 
                    "MW2208": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸下降异常，请检查X212,Y212"
                    }, 
                    "MW2209": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸异常，请检查X211,X212"
                    }, 
                    "MW2210": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1松开异常，请检查X213、Y213"
                    }, 
                    "MW2211": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1夹紧异常，请检查X214、Y214"
                    }, 
                    "MW2212": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1异常，请检查X213、X214"
                    }, 
                    "MW2213": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2松开异常，请检查X215、Y213"
                    }, 
                    "MW2214": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2夹紧异常，请检查X216、Y214"
                    }, 
                    "MW2215": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2异常，请检查X215、X216"
                    }, 
                    "MW2216": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸上升异常，请检查X221,Y221"
                    }, 
                    "MW2217": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸下降异常，请检查X222,Y222"
                    }, 
                    "MW2218": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸异常，请检查X221,X222"
                    }, 
                    "MW2219": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1松开异常，请检查X223、Y223"
                    }, 
                    "MW2220": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1夹紧异常，请检查X224、Y224"
                    }, 
                    "MW2221": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1异常，请检查X223、X224"
                    }, 
                    "MW2222": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2松开异常，请检查X225、Y223"
                    }, 
                    "MW2223": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2夹紧异常，请检查X226、Y224"
                    }, 
                    "MW2224": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2异常，请检查X225、X226"
                    }, 
                    "MW2225": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1上升异常，请检查X230、Y230"
                    }, 
                    "MW2226": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1下降异常，请检查X231、Y231"
                    }, 
                    "MW2227": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1异常，请检查X230、X231"
                    }, 
                    "MW2228": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪1松开异常，请检查X232、Y232"
                    }, 
                    "MW2229": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪1夹紧异常，请检查X232、Y233"
                    }, 
                    "MW2230": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event230"
                    }, 
                    "MW2231": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1原点异常，请检查X234、Y234"
                    }, 
                    "MW2232": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1动点异常，请检查X235、Y235"
                    }, 
                    "MW2233": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1异常，请检查X234、X235"
                    }, 
                    "MW2234": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2上升异常，请检查X240、Y240"
                    }, 
                    "MW2235": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2下降异常，请检查X241、Y241"
                    }, 
                    "MW2236": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2异常，请检查X240、X241"
                    }, 
                    "MW2237": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪2松开异常，请检查X242、Y242"
                    }, 
                    "MW2238": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪2夹紧异常，请检查X242、Y243"
                    }, 
                    "MW2239": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event239"
                    }, 
                    "MW2240": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2原点异常，请检查X244、Y244"
                    }, 
                    "MW2241": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2动点异常，请检查X245、Y245"
                    }, 
                    "MW2242": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2异常，请检查X244、X245"
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
                        "desc": " 工位2主轨道A有产品条码为空报警"
                    }, 
                    "MW2251": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A治具ID读取失败报警"
                    }, 
                    "MW2252": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A治具ID读取超时报警"
                    }, 
                    "MW2253": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B有产品条码为空报警"
                    }, 
                    "MW2254": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B治具ID读取失败报警"
                    }, 
                    "MW2255": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B治具ID读取超时报警"
                    }, 
                    "MW2256": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A上下气缸1压PCBA异常报警"
                    }, 
                    "MW2257": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A上下气缸2压PCBA异常报警"
                    }, 
                    "MW2258": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B上下气缸1压PCBA异常报警"
                    }, 
                    "MW2259": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B上下气缸2压PCBA异常报警"
                    }, 
                    "MW2260": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A产品1扫条码失败报警"
                    }, 
                    "MW2261": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A产品3扫条码失败报警"
                    }, 
                    "MW2262": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B产品1扫条码失败报警"
                    }, 
                    "MW2263": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B产品3扫条码失败报警"
                    }, 
                    "MW2264": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2265": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2266": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道A到位阻挡下降超时"
                    }, 
                    "MW2267": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道B到位阻挡下降超时"
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
                        "desc": " 装PCBA工位2轨道A有产品条码为空"
                    }, 
                    "MW2271": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2轨道B有产品条码为空"
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
                        "desc": " 压PCBA工位轨道A顶升气缸上升异常，请检查X251、Y251"
                    }, 
                    "MW2281": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A顶升气缸下降异常，请检查X252、Y252"
                    }, 
                    "MW2282": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A顶升气缸异常，请检查X251、X252"
                    }, 
                    "MW2283": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸上升异常，请检查X255、Y255"
                    }, 
                    "MW2284": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸下降异常，请检查X256、Y256"
                    }, 
                    "MW2285": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸异常，请检查X255、X256"
                    }, 
                    "MW2286": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A阻挡气缸放板超时"
                    }, 
                    "MW2287": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B阻挡气缸放板超时"
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
                        "desc": " 轨道A-返治具升降机上下气缸上升异常，请检查X82、Y82"
                    }, 
                    "MW2291": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-返治具升降机上下气缸下降异常，请检查X83、Y83"
                    }, 
                    "MW2292": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-返治具升降机上下气缸异常，请检查X82、X83"
                    }, 
                    "MW2293": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸上升异常，请检查X86、Y86"
                    }, 
                    "MW2294": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸下降异常，请检查X87、Y87"
                    }, 
                    "MW2295": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸异常，请检查X86、X87"
                    }, 
                    "MW2296": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A返治具升降机皮带运转超时"
                    }, 
                    "MW2297": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B返治具升降机皮带运转超时"
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
                ("D05", "MP18", "MP-TJ-APA-001"): {
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
                        "desc": " 工位1安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2052": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
                    }, 
                    "MW2053": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 返治具升降机安全门打开，请人工确认_x000D_\n在安全情况下，点动复位，清除报警"
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 工位-1-轨道A读卡超时！"
                    }, 
                    "MW2086": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-1-轨道B读卡超时！"
                    }, 
                    "MW2087": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-2-轨道A读卡超时！"
                    }, 
                    "MW2088": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位-2-轨道B读卡超时！"
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
                        "desc": " 工位1副轨道A顶升气缸上升异常，请检查X31,Y31"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A顶升气缸下降异常，请检查X32,Y32"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A顶升气缸异常，请检查X31,X32"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸上升异常，请检查X34,Y34"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸下降异常，请检查X35,Y35"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B顶升气缸异常，请检查X34,X35"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸上升异常，请检查X41,Y41"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸下降异常，请检查X42,Y42"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A顶升气缸异常，请检查X41,X42"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1松开异常，请检查X43、Y43"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1夹紧异常，请检查X44、Y44"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸1异常，请检查X43、X44"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2松开异常，请检查X45、Y43"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2夹紧异常，请检查X46、Y44"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A底壳定位气缸2异常，请检查X45、X46"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸上升异常，请检查X51,Y51"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸下降异常，请检查X52,Y52"
                    }, 
                    "MW2118": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B顶升气缸异常，请检查X51,X52"
                    }, 
                    "MW2119": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1松开异常，请检查X53、Y53"
                    }, 
                    "MW2120": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1夹紧异常，请检查X54、Y54"
                    }, 
                    "MW2121": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸1异常，请检查X53、X54"
                    }, 
                    "MW2122": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2松开异常，请检查X55、Y53"
                    }, 
                    "MW2123": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2夹紧异常，请检查X56、Y54"
                    }, 
                    "MW2124": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B底壳定位气缸2异常，请检查X55、X56"
                    }, 
                    "MW2125": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1上升异常，请检查X60、Y60"
                    }, 
                    "MW2126": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1下降异常，请检查X61、Y61"
                    }, 
                    "MW2127": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸1异常，请检查X60、X61"
                    }, 
                    "MW2128": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪1松开异常，请检查X62、Y62"
                    }, 
                    "MW2129": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪1夹紧异常，请检查X62、Y63"
                    }, 
                    "MW2130": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1原点异常，请检查X64、Y64"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1动点异常，请检查X65、Y65"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸1异常，请检查X64、X65"
                    }, 
                    "MW2134": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2上升异常，请检查X70、Y70"
                    }, 
                    "MW2135": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2下降异常，请检查X71、Y71"
                    }, 
                    "MW2136": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手压PCBA上下气缸2异常，请检查X70、X71"
                    }, 
                    "MW2137": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪2松开异常，请检查X72、Y72"
                    }, 
                    "MW2138": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手夹爪2夹紧异常，请检查X72、Y73"
                    }, 
                    "MW2139": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event139"
                    }, 
                    "MW2140": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2原点异常，请检查X74、Y74"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2动点异常，请检查X75、Y75"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1机械手旋转气缸2异常，请检查X74、X75"
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
                        "desc": " 工位1主轨道A有产品条码为空报警"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A治具ID读取失败报警"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A治具ID读取超时报警"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B有产品条码为空报警"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B治具ID读取失败报警"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B治具ID读取超时报警"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A上下气缸1压PCBA异常报警"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道A上下气缸2压PCBA异常报警"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B上下气缸1压PCBA异常报警"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1主轨道B上下气缸2压PCBA异常报警"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A产品2扫条码失败报警"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道A产品4扫条码失败报警"
                    }, 
                    "MW2162": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B产品2扫条码失败报警"
                    }, 
                    "MW2163": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位1副轨道B产品4扫条码失败报警"
                    }, 
                    "MW2164": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1副轨道A到位阻挡下降超时"
                    }, 
                    "MW2165": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1副轨道B到位阻挡下降超时"
                    }, 
                    "MW2166": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2167": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2168": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道A到位阻挡下降超时"
                    }, 
                    "MW2169": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位1主轨道B到位阻挡下降超时"
                    }, 
                    "MW2170": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2171": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2172": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道A到位阻挡下降超时"
                    }, 
                    "MW2173": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2主轨道B到位阻挡下降超时"
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
                        "desc": " 工位2副轨道A顶升气缸上升异常，请检查X201,Y201"
                    }, 
                    "MW2202": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A顶升气缸下降异常，请检查X202,Y202"
                    }, 
                    "MW2203": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A顶升气缸异常，请检查X201,X202"
                    }, 
                    "MW2204": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸上升异常，请检查X204,Y204"
                    }, 
                    "MW2205": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸下降异常，请检查X205,Y205"
                    }, 
                    "MW2206": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B顶升气缸异常，请检查X204,X205"
                    }, 
                    "MW2207": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸上升异常，请检查X211,Y211"
                    }, 
                    "MW2208": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸下降异常，请检查X212,Y212"
                    }, 
                    "MW2209": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A顶升气缸异常，请检查X211,X212"
                    }, 
                    "MW2210": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1松开异常，请检查X213、Y213"
                    }, 
                    "MW2211": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1夹紧异常，请检查X214、Y214"
                    }, 
                    "MW2212": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸1异常，请检查X213、X214"
                    }, 
                    "MW2213": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2松开异常，请检查X215、Y213"
                    }, 
                    "MW2214": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2夹紧异常，请检查X216、Y214"
                    }, 
                    "MW2215": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A底壳定位气缸2异常，请检查X215、X216"
                    }, 
                    "MW2216": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸上升异常，请检查X221,Y221"
                    }, 
                    "MW2217": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸下降异常，请检查X222,Y222"
                    }, 
                    "MW2218": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B顶升气缸异常，请检查X221,X222"
                    }, 
                    "MW2219": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1松开异常，请检查X223、Y223"
                    }, 
                    "MW2220": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1夹紧异常，请检查X224、Y224"
                    }, 
                    "MW2221": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸1异常，请检查X223、X224"
                    }, 
                    "MW2222": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2松开异常，请检查X225、Y223"
                    }, 
                    "MW2223": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2夹紧异常，请检查X226、Y224"
                    }, 
                    "MW2224": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B底壳定位气缸2异常，请检查X225、X226"
                    }, 
                    "MW2225": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1上升异常，请检查X230、Y230"
                    }, 
                    "MW2226": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1下降异常，请检查X231、Y231"
                    }, 
                    "MW2227": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸1异常，请检查X230、X231"
                    }, 
                    "MW2228": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪1松开异常，请检查X232、Y232"
                    }, 
                    "MW2229": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪1夹紧异常，请检查X232、Y233"
                    }, 
                    "MW2230": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event230"
                    }, 
                    "MW2231": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1原点异常，请检查X234、Y234"
                    }, 
                    "MW2232": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1动点异常，请检查X235、Y235"
                    }, 
                    "MW2233": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸1异常，请检查X234、X235"
                    }, 
                    "MW2234": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2上升异常，请检查X240、Y240"
                    }, 
                    "MW2235": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2下降异常，请检查X241、Y241"
                    }, 
                    "MW2236": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手压PCBA上下气缸2异常，请检查X240、X241"
                    }, 
                    "MW2237": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪2松开异常，请检查X242、Y242"
                    }, 
                    "MW2238": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手夹爪2夹紧异常，请检查X242、Y243"
                    }, 
                    "MW2239": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event239"
                    }, 
                    "MW2240": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2原点异常，请检查X244、Y244"
                    }, 
                    "MW2241": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2动点异常，请检查X245、Y245"
                    }, 
                    "MW2242": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2机械手旋转气缸2异常，请检查X244、X245"
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
                        "desc": " 工位2主轨道A有产品条码为空报警"
                    }, 
                    "MW2251": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A治具ID读取失败报警"
                    }, 
                    "MW2252": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A治具ID读取超时报警"
                    }, 
                    "MW2253": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B有产品条码为空报警"
                    }, 
                    "MW2254": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B治具ID读取失败报警"
                    }, 
                    "MW2255": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B治具ID读取超时报警"
                    }, 
                    "MW2256": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A上下气缸1压PCBA异常报警"
                    }, 
                    "MW2257": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道A上下气缸2压PCBA异常报警"
                    }, 
                    "MW2258": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B上下气缸1压PCBA异常报警"
                    }, 
                    "MW2259": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2主轨道B上下气缸2压PCBA异常报警"
                    }, 
                    "MW2260": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A产品1扫条码失败报警"
                    }, 
                    "MW2261": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道A产品3扫条码失败报警"
                    }, 
                    "MW2262": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B产品1扫条码失败报警"
                    }, 
                    "MW2263": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 工位2副轨道B产品3扫条码失败报警"
                    }, 
                    "MW2264": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道A前缓冲阻挡下降超时"
                    }, 
                    "MW2265": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道B前缓冲阻挡下降超时"
                    }, 
                    "MW2266": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道A到位阻挡下降超时"
                    }, 
                    "MW2267": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2副轨道B到位阻挡下降超时"
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
                        "desc": " 装PCBA工位2轨道A有产品条码为空"
                    }, 
                    "MW2271": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装PCBA工位2轨道B有产品条码为空"
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
                        "desc": " 压PCBA工位轨道A顶升气缸上升异常，请检查X251、Y251"
                    }, 
                    "MW2281": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A顶升气缸下降异常，请检查X252、Y252"
                    }, 
                    "MW2282": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A顶升气缸异常，请检查X251、X252"
                    }, 
                    "MW2283": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸上升异常，请检查X255、Y255"
                    }, 
                    "MW2284": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸下降异常，请检查X256、Y256"
                    }, 
                    "MW2285": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B顶升气缸异常，请检查X255、X256"
                    }, 
                    "MW2286": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道A阻挡气缸放板超时"
                    }, 
                    "MW2287": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压PCBA工位轨道B阻挡气缸放板超时"
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
                        "desc": " 轨道A-返治具升降机上下气缸上升异常，请检查X82、Y82"
                    }, 
                    "MW2291": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-返治具升降机上下气缸下降异常，请检查X83、Y83"
                    }, 
                    "MW2292": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-返治具升降机上下气缸异常，请检查X82、X83"
                    }, 
                    "MW2293": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸上升异常，请检查X86、Y86"
                    }, 
                    "MW2294": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸下降异常，请检查X87、Y87"
                    }, 
                    "MW2295": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-返治具升降机上下气缸异常，请检查X86、X87"
                    }, 
                    "MW2296": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A返治具升降机皮带运转超时"
                    }, 
                    "MW2297": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B返治具升降机皮带运转超时"
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
                ("D05", "MP18", "MP-TJ-ACA-002"): {
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
                        "desc": " 取上盖检测机械手真空报警，_x000D_\n可在异常解除里选择“跳过”_x000D_\n机械手继续完成取盖动作！"
                    }, 
                    "MW2021": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖吸嘴真空报警，_x000D_\n可在异常解除里选择“跳过”_x000D_\n机械手继续完成取盖动作！"
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 压上盖光纤检测浮高报警，请人工确认，点动复位清除"
                    }, 
                    "MW2100": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event100"
                    }, 
                    "MW2101": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道A顶升气缸上升异常，请检查X31、Y31"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道A顶升气缸下降异常，请检查X32、Y32"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道A顶升气缸异常，请检查X31、X32"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道B顶升气缸上升异常，请检查X36、Y36"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道B顶升气缸下降异常，请检查X37、Y37"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道B顶升气缸异常，请检查X36、X37"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道A顶升气缸上升异常，请检查X52、Y51"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道A顶升气缸下降异常，请检查X52、Y52"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event109"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道B顶升气缸上升异常，请检查X57、Y56"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道B顶升气缸下降异常，请检查X57、Y57"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event112"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴1吸取异常，请检查X60、Y60"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴1爆破异常，请检查X60、Y61"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event115"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴2吸取异常，请检查X62、Y62"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴2爆破异常，请检查X62、Y63"
                    }, 
                    "MW2118": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event118"
                    }, 
                    "MW2119": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴3吸取异常，请检查X64、Y64"
                    }, 
                    "MW2120": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴3爆破异常，请检查X64、Y65"
                    }, 
                    "MW2121": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event121"
                    }, 
                    "MW2122": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴4吸取异常，请检查X66、Y66"
                    }, 
                    "MW2123": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手吸嘴4爆破异常，请检查X66、Y67"
                    }, 
                    "MW2124": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event124"
                    }, 
                    "MW2125": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手Z轴气缸上升异常，请检查X70、Y70"
                    }, 
                    "MW2126": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手Z轴气缸下降异常，请检查X71、Y71"
                    }, 
                    "MW2127": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取上盖机械手Z轴气缸异常，请检查X70、X71"
                    }, 
                    "MW2128": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘X轴气缸左移异常，请检查X72、Y72"
                    }, 
                    "MW2129": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘X轴气缸右移异常，请检查X73、Y73"
                    }, 
                    "MW2130": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘X轴气缸异常，请检查X72、X73"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘Z轴气缸上升异常，请检查X74、Y74"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘Z轴气缸下降异常，请检查X75、Y75"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘Z轴气缸异常，请检查X74、X75"
                    }, 
                    "MW2134": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘吸嘴吸取异常，请检查X76、Y76"
                    }, 
                    "MW2135": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取空料盘吸嘴爆破异常，请检查X76、Y77"
                    }, 
                    "MW2136": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event136"
                    }, 
                    "MW2137": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴1吸取异常，请检查X80、Y80"
                    }, 
                    "MW2138": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴1爆破异常，请检查X80、Y81"
                    }, 
                    "MW2139": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event139"
                    }, 
                    "MW2140": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴2吸取异常，请检查X82、Y82"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴2爆破异常，请检查X82、Y83"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event142"
                    }, 
                    "MW2143": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴3吸取异常，请检查X84、Y84"
                    }, 
                    "MW2144": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴3爆破异常，请检查X84、Y85"
                    }, 
                    "MW2145": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event145"
                    }, 
                    "MW2146": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴4吸取异常，请检查X86、Y86"
                    }, 
                    "MW2147": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖机械手吸嘴4爆破异常，请检查X86、Y87"
                    }, 
                    "MW2148": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event148"
                    }, 
                    "MW2149": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道切换气缸伸出异常，请检查X40、Y40"
                    }, 
                    "MW2150": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道切换气缸退回异常，请检查X41、Y41"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道切换气缸异常，请检查X40、X41"
                    }, 
                    "MW2152": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位产品定位气缸松开异常，请检查X42、Y42"
                    }, 
                    "MW2153": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位产品定位气缸夹紧异常，请检查X43、Y43"
                    }, 
                    "MW2154": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位产品定位气缸异常，请检查X42、X43"
                    }, 
                    "MW2155": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖前后气缸后退异常，请检查X44、Y44"
                    }, 
                    "MW2156": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖前后气缸前进异常，请检查X45、Y45"
                    }, 
                    "MW2157": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖前后气缸异常报警！！！"
                    }, 
                    "MW2158": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖上下气缸上升异常，请检查X46、Y46"
                    }, 
                    "MW2159": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖上下气缸下降异常，请检查X47、Y47"
                    }, 
                    "MW2160": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位压上盖上下气缸异常报警！！"
                    }, 
                    "MW2161": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2162": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event162"
                    }, 
                    "MW2163": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道A_ID读取异常"
                    }, 
                    "MW2164": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道B_ID读取异常"
                    }, 
                    "MW2165": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " CCD检测触发超时"
                    }, 
                    "MW2166": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖气缸下降状态，但是装上盖气缸再抓紧状态，_x000D_\n请检查装上盖抓夹上有无产品，如果有请取出产品_x000D_\n后复位，如果无产品请直接复位！！！"
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
                        "desc": " 提示：上盖没料提示，请及时上料！！！"
                    }, 
                    "MW2170": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 取料盘失败报警"
                    }, 
                    "MW2171": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 空料盘收集区满料报警"
                    }, 
                    "MW2172": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道A放板超时"
                    }, 
                    "MW2173": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压上盖工位轨道B放板超时"
                    }, 
                    "MW2174": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道A放板超时"
                    }, 
                    "MW2175": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 装上盖工位轨道B放板超时"
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
                        "desc": " 放上盖工位机械手Z轴气缸上升异常，请检查“X50”，“Y50”"
                    }, 
                    "MW2181": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖工位机械手Z轴气缸下降异常，请检查“X51”，“Y51”"
                    }, 
                    "MW2182": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 放上盖工位机械手Z轴气缸异常报警！！！"
                    }, 
                    "MW2183": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 料盘定位气缸伸出报警，请检查X206,输出Y206，Y207."
                    }, 
                    "MW2184": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 料盘定位气缸伸出报警，请检查X206,输出Y206，Y207."
                    }, 
                    "MW2185": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 料盘定位气缸伸出报警，请检查X206,输出Y206，Y207."
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
                ("D05", "MP18", "MP-TJ-CCD-003"): {
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " Step检测轨道A顶升气缸上升异常，请检查“X31”或“Y31”，按复位消除报警"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A顶升气缸下降异常，请检查“X32”或“Y32”，按复位消除报警"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A顶升气缸异常报警！"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A合拢气缸松开异常，请检查“X34”或“Y34”，按复位消除报警"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A合拢气缸夹紧异常，请检查“X34”或“Y34”，按复位消除报警"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A合拢气缸异常报警！！！"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道A放板超时，请确认，按“复位”消除报警"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event109"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-Step检测ID读卡异常，按“复位”消除报警！"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A-Step检测治具条码绑定异常，按“复位”消除报警！"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
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
                        "desc": " 轨道A-STEP检测触发超时，请检查软件是否打开！！！"
                    }, 
                    "MW2121": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A夹爪复位时处于夹紧未松开，请确认！"
                    }, 
                    "MW2122": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B夹爪复位时处于夹紧未松开，请确认！"
                    }, 
                    "MW2123": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A治具读取ID为空，请确认！"
                    }, 
                    "MW2124": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B治具读取ID为空，请确认！"
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
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event131"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event132"
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
                        "desc": " Step检测轨道B顶升气缸上升异常，请检查“X40”或“Y40”，按复位消除报警"
                    }, 
                    "MW2202": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B顶升气缸下降异常，请检查“X41”或“Y41”，按复位消除报警"
                    }, 
                    "MW2203": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B顶升气缸异常报警！"
                    }, 
                    "MW2204": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B合拢气缸松开异常，请检查“X42”或“Y42”，按复位消除报警"
                    }, 
                    "MW2205": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B合拢气缸夹紧异常，请检查“X42”或“Y43”，按复位消除报警"
                    }, 
                    "MW2206": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B合拢气缸异常报警！！！"
                    }, 
                    "MW2207": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Step检测轨道B放板超时，请确认，按“复位”消除报警"
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
                        "desc": " 轨道B-Step检测ID读卡异常，按“复位”消除报警！"
                    }, 
                    "MW2211": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event211"
                    }, 
                    "MW2212": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B-Step检测治具条码绑定异常，按“复位”消除报警！"
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
                        "desc": " 轨道B-STEP检测触发超时，请检查软件是否打开！！！"
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
                ("D05", "MP18", "MP-TJ-ATM-061"): {
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
                        "desc": " 不良轨道满料超时，请处理不良品！"
                    }, 
                    "MW2071": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 轨道A镭雕检测位顶升气缸上升异常，请检查“X32”或“Y32”，按复位消除报警"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位顶升气缸下降异常，请检查“X33”或“Y33”，按复位消除报警"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位顶升气缸异常报警！"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位定位气缸松开异常，请检查“X35”或“Y35”，按复位消除报警"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位定位气缸夹紧异常，请检查“X34”或“Y34”，按复位消除报警"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位定位气缸异常报警！"
                    }, 
                    "MW2107": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位ID读卡失败，请按“复位”消除报警！"
                    }, 
                    "MW2108": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位条码绑定失败异常，请按“复位”消除报警！"
                    }, 
                    "MW2109": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位触发超时，请确认软件是否打开！"
                    }, 
                    "MW2110": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A镭雕检测位放治具超时，请确认是否卡治具！"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位顶升气缸上升异常，请检查“X42”或“Y42”，按复位消除报警"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B雕检测位顶升气缸下降异常，请检查“X43”或“Y43”，按复位消除报警"
                    }, 
                    "MW2113": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位顶升气缸异常报警！"
                    }, 
                    "MW2114": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位定位气缸松开异常，请检查“X45”或“Y45”，按复位消除报警"
                    }, 
                    "MW2115": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位定位气缸夹紧异常，请检查“X44”或“Y44”，按复位消除报警"
                    }, 
                    "MW2116": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位定位气缸异常报警！"
                    }, 
                    "MW2117": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位ID读卡失败，请按“复位”消除报警！"
                    }, 
                    "MW2118": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位条码绑定失败异常，请按“复位”消除报警！"
                    }, 
                    "MW2119": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位触发超时，请确认软件是否打开！"
                    }, 
                    "MW2120": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B镭雕检测位放治具超时，请确认是否卡治具！"
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
                        "desc": " 轨道A镭雕检测位前缓冲放治具超时，请确认是否卡治具！"
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
                        "desc": " 轨道A下机位前缓冲放板超时，请确认是否卡治具！！！，按“复位”消除报警"
                    }, 
                    "MW2130": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位前缓冲放板超时，请确认是否卡治具！！！，按“复位”消除报警"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位顶升气缸上升异常，请检查“X51”或“Y51”，按复位消除报警！"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位顶升气缸下降异常，请检查“X52”或“Y52”，按复位消除报警！"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位顶升气缸异常报警！"
                    }, 
                    "MW2134": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位顶升位ID读卡失败，请按“复位”消除报警"
                    }, 
                    "MW2135": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位放板超时，请确认是否卡治具！！！，按“复位”消除报警"
                    }, 
                    "MW2136": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A下机位顶升位ID读卡超时，请按“复位”消除报警"
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
                        "desc": " 轨道B下机位顶升气缸上升异常，请检查“X54”或“Y54”，按复位消除报警！"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位顶升气缸下降异常，请检查“X55”或“Y55”，按复位消除报警！"
                    }, 
                    "MW2143": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位顶升气缸异常报警！"
                    }, 
                    "MW2144": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位顶升位ID读卡失败，请按“复位”消除报警"
                    }, 
                    "MW2145": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位放板超时，请确认是否卡治具！！！，按“复位”消除报警"
                    }, 
                    "MW2146": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B下机位顶升位ID读卡超时，请按“复位”消除报警"
                    }, 
                    "MW2147": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 自动下机机械手旋转气缸复位异常，请检查“X56”或“Y56”，按复位消除报警！"
                    }, 
                    "MW2148": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 自动下机机械手旋转气缸动作异常，请检查“X57”或“Y57”，按复位消除报警！"
                    }, 
                    "MW2149": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 自动下机机械手旋转气缸异常报警！"
                    }, 
                    "MW2150": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event150"
                    }, 
                    "MW2151": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 自动下机机械手夹爪1松开异常，请检查“X61”或“Y61”，按复位消除报警！"
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
                        "desc": " 轨道A升降机上升异常，请检查“X72”或“Y72”，按复位消除报警"
                    }, 
                    "MW2172": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A升降机下降异常，请检查“X73”或“Y73”，按复位消除报警"
                    }, 
                    "MW2173": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A升降机气缸异常报警！"
                    }, 
                    "MW2174": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道A升降机升降机马达运转超时报警！请确认是否卡治具，_x000D_\n按“复位”消除报警"
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
                        "desc": " 轨道B升降机上升异常，请检查“X76”或“Y76”，按复位消除报警"
                    }, 
                    "MW2182": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B升降机下降异常，请检查“X77”或“Y77”，按复位消除报警"
                    }, 
                    "MW2183": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B升降机气缸异常报警！"
                    }, 
                    "MW2184": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B升降机升降机马达运转超时报警！请确认是否卡治具，_x000D_\n按“复位”消除报警"
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
                ("D05", "MP18", "MP-TJ-CCD-004"): {
                    "MW2000": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2001": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2002": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                    }, 
                    "MW2003": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2004": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2005": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2006": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2007": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2008": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2009": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 进料工位缺料"
                    }, 
                    "MW2010": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸上限异常"
                    }, 
                    "MW2011": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸下限异常"
                    }, 
                    "MW2012": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸异常"
                    }, 
                    "MW2013": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸上限异常"
                    }, 
                    "MW2014": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸下限异常"
                    }, 
                    "MW2015": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸异常"
                    }, 
                    "MW2016": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸上限异常"
                    }, 
                    "MW2017": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸下限异常"
                    }, 
                    "MW2018": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸异常"
                    }, 
                    "MW2019": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸上限异常"
                    }, 
                    "MW2020": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸下限异常"
                    }, 
                    "MW2021": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸异常"
                    }, 
                    "MW2022": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸上限异常"
                    }, 
                    "MW2023": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸下限异常"
                    }, 
                    "MW2024": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸异常"
                    }, 
                    "MW2025": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸上限异常"
                    }, 
                    "MW2026": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸下限异常"
                    }, 
                    "MW2027": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸异常"
                    }, 
                    "MW2028": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸左限异常"
                    }, 
                    "MW2029": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸右限异常"
                    }, 
                    "MW2030": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸异常"
                    }, 
                    "MW2031": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸上限异常"
                    }, 
                    "MW2032": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸下限异常"
                    }, 
                    "MW2033": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸异常"
                    }, 
                    "MW2034": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸原点异常"
                    }, 
                    "MW2035": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸动点异常"
                    }, 
                    "MW2036": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸异常"
                    }, 
                    "MW2037": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸原点异常"
                    }, 
                    "MW2038": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸动点异常"
                    }, 
                    "MW2039": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸异常"
                    }, 
                    "MW2040": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸原点异常"
                    }, 
                    "MW2041": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸动点异常"
                    }, 
                    "MW2042": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸异常"
                    }, 
                    "MW2043": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸原点异常"
                    }, 
                    "MW2044": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸动点异常"
                    }, 
                    "MW2045": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸异常"
                    }, 
                    "MW2046": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸原点异常"
                    }, 
                    "MW2047": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸动点异常"
                    }, 
                    "MW2048": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸异常"
                    }, 
                    "MW2049": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 点胶CCD检测报警"
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
                        "desc": " 提示：空料盘框满料提示"
                    }, 
                    "MW2056": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event56"
                    }, 
                    "MW2057": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2058": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸松开异常"
                    }, 
                    "MW2059": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸夹紧异常"
                    }, 
                    "MW2060": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸异常"
                    }, 
                    "MW2061": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸松开异常"
                    }, 
                    "MW2062": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸夹紧异常"
                    }, 
                    "MW2063": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸异常"
                    }, 
                    "MW2064": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸松开异常"
                    }, 
                    "MW2065": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸夹紧异常"
                    }, 
                    "MW2066": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸异常"
                    }, 
                    "MW2067": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸松开异常"
                    }, 
                    "MW2068": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸夹紧异常"
                    }, 
                    "MW2069": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸异常"
                    }, 
                    "MW2070": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event70"
                    }, 
                    "MW2071": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 取产品机械手吸产品真空报警，_x000D_\n可在异常解除里选择“跳过”，继续机械手动作！"
                    }, 
                    "MW2077": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位真空报警，_x000D_\n可在异常解除里选择“跳过”，继续机械手动作！"
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
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2081": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2082": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2083": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2084": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2085": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2086": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2087": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2088": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2089": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
                    }, 
                    "MW2090": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
                    }, 
                    "MW2091": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
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
                        "desc": " CASE检测-CCD触发超时！"
                    }, 
                    "MW2096": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 出料升降机出料超时！"
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
                        "desc": " Event101"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event102"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event103"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event104"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event105"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event106"
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
                        "desc": " Event110"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event111"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event112"
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
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event131"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event132"
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
                    }
                }, 
                ("D05", "MP18", "MP-TJ-ACA-001"): {
                    "MW2000": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2001": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2002": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
                    }, 
                    "MW2003": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2004": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2005": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2006": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2007": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2008": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2009": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 进料工位缺料"
                    }, 
                    "MW2010": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸上限异常"
                    }, 
                    "MW2011": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸下限异常"
                    }, 
                    "MW2012": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_PCB治具顶升气缸异常"
                    }, 
                    "MW2013": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸上限异常"
                    }, 
                    "MW2014": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸下限异常"
                    }, 
                    "MW2015": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_PCB治具顶升气缸异常"
                    }, 
                    "MW2016": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸上限异常"
                    }, 
                    "MW2017": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸下限异常"
                    }, 
                    "MW2018": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道1升降机气缸异常"
                    }, 
                    "MW2019": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸上限异常"
                    }, 
                    "MW2020": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸下限异常"
                    }, 
                    "MW2021": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道升降机.轨道2升降机气缸异常"
                    }, 
                    "MW2022": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸上限异常"
                    }, 
                    "MW2023": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸下限异常"
                    }, 
                    "MW2024": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道1_产品治具顶升气缸异常"
                    }, 
                    "MW2025": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸上限异常"
                    }, 
                    "MW2026": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸下限异常"
                    }, 
                    "MW2027": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道顶升.轨道2_产品治具顶升气缸异常"
                    }, 
                    "MW2028": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸左限异常"
                    }, 
                    "MW2029": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸右限异常"
                    }, 
                    "MW2030": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " .吸空料盘平移气缸异常"
                    }, 
                    "MW2031": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸上限异常"
                    }, 
                    "MW2032": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸下限异常"
                    }, 
                    "MW2033": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸空料盘上下气缸异常"
                    }, 
                    "MW2034": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸原点异常"
                    }, 
                    "MW2035": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸动点异常"
                    }, 
                    "MW2036": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1旋转气缸异常"
                    }, 
                    "MW2037": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸原点异常"
                    }, 
                    "MW2038": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸动点异常"
                    }, 
                    "MW2039": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2旋转气缸异常"
                    }, 
                    "MW2040": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸原点异常"
                    }, 
                    "MW2041": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸动点异常"
                    }, 
                    "MW2042": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3旋转气缸异常"
                    }, 
                    "MW2043": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸原点异常"
                    }, 
                    "MW2044": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸动点异常"
                    }, 
                    "MW2045": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4旋转气缸异常"
                    }, 
                    "MW2046": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸原点异常"
                    }, 
                    "MW2047": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸动点异常"
                    }, 
                    "MW2048": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位翻转气缸异常"
                    }, 
                    "MW2049": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 点胶CCD检测报警"
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
                        "desc": " 提示：空料盘框满料提示"
                    }, 
                    "MW2056": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event56"
                    }, 
                    "MW2057": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2058": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸松开异常"
                    }, 
                    "MW2059": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸夹紧异常"
                    }, 
                    "MW2060": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪1气缸异常"
                    }, 
                    "MW2061": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸松开异常"
                    }, 
                    "MW2062": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸夹紧异常"
                    }, 
                    "MW2063": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪2气缸异常"
                    }, 
                    "MW2064": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸松开异常"
                    }, 
                    "MW2065": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸夹紧异常"
                    }, 
                    "MW2066": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪3气缸异常"
                    }, 
                    "MW2067": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸松开异常"
                    }, 
                    "MW2068": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸夹紧异常"
                    }, 
                    "MW2069": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 夹爪4气缸异常"
                    }, 
                    "MW2070": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event70"
                    }, 
                    "MW2071": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 取产品机械手吸产品真空报警，_x000D_\n可在异常解除里选择“跳过”，继续机械手动作！"
                    }, 
                    "MW2077": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 过渡位真空报警，_x000D_\n可在异常解除里选择“跳过”，继续机械手动作！"
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
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2081": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2082": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸1极限异常！_x000D_\n请检查气缸输入输出点X90.X91.Y230.Y231"
                    }, 
                    "MW2083": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2084": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2085": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸2极限异常！_x000D_\n请检查气缸输入输出点X92.X93.Y232.Y233"
                    }, 
                    "MW2086": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2087": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2088": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸3极限异常！_x000D_\n请检查气缸输入输出点X94.X95.Y234.Y235"
                    }, 
                    "MW2089": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
                    }, 
                    "MW2090": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
                    }, 
                    "MW2091": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸嘴上下气缸4极限异常！_x000D_\n请检查气缸输入输出点X96.X97.Y236.Y237"
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
                        "desc": " CASE检测-CCD触发超时！"
                    }, 
                    "MW2096": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 出料升降机出料超时！"
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
                        "desc": " Event101"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event102"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event103"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event104"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event105"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event106"
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
                        "desc": " Event110"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event111"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event112"
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
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event131"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event132"
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
                    }
                }, 
                ("D05", "MP18", "MP-TJ-ABL-007"): {
                    "MW2000": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 变距气缸张开感应异常"
                    }, 
                    "MW2001": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 变距气缸合拢感应异常"
                    }, 
                    "MW2002": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 变距气缸信号异常"
                    }, 
                    "MW2003": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压标签气缸上限异常"
                    }, 
                    "MW2004": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压标签气缸下限异常"
                    }, 
                    "MW2005": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 压标签气缸信号异常"
                    }, 
                    "MW2006": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 脱标签气缸前限异常"
                    }, 
                    "MW2007": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 脱标签气缸后限异常"
                    }, 
                    "MW2008": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 脱标签气缸信号异常"
                    }, 
                    "MW2009": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道1顶升气缸上限异常"
                    }, 
                    "MW2010": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道1顶升气缸下限异常"
                    }, 
                    "MW2011": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道1顶升气缸信号异常"
                    }, 
                    "MW2012": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道2顶升气缸上限异常"
                    }, 
                    "MW2013": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道2顶升气缸下限异常"
                    }, 
                    "MW2014": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签轨道2顶升气缸信号异常"
                    }, 
                    "MW2015": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道1顶升气缸上限异常"
                    }, 
                    "MW2016": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道1顶升气缸下限异常"
                    }, 
                    "MW2017": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道1顶升气缸信号异常"
                    }, 
                    "MW2018": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道2顶升气缸上限异常"
                    }, 
                    "MW2019": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道2顶升气缸下限异常"
                    }, 
                    "MW2020": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码轨道2顶升气缸信号异常"
                    }, 
                    "MW2021": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 吸标签真空报警-_x000D_\n可在异常解除里选择“跳过”_x000D_\n机械手继续完成下一步动作！"
                    }, 
                    "MW2022": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event22"
                    }, 
                    "MW2023": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event"
                    }, 
                    "MW2024": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签Y轴报警"
                    }, 
                    "MW2025": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 贴标签Z轴报警"
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
                        "desc": " 标签缺料报警--是否切换标签送料方式！_x000D_\n请在异常解除里切换，切换后，以定位的方式连续送料，_x000D_\n定位送料次数到达设定次数后再次缺料报警，_x000D_\n请及时更换标签！"
                    }, 
                    "MW2040": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道1贴条码位_ID读取异常"
                    }, 
                    "MW2041": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道2贴条码位_ID读取异常"
                    }, 
                    "MW2042": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道1扫条码位_ID读取异常"
                    }, 
                    "MW2043": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道2扫条码位_ID读取异常"
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
                        "desc": " 扫条码位_轨道1读卡失败"
                    }, 
                    "MW2061": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码位_轨道2读卡失败"
                    }, 
                    "MW2062": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码位_轨道1扫码失败"
                    }, 
                    "MW2063": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 扫条码位_轨道2扫码失败"
                    }, 
                    "MW2064": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道1-扫码失败"
                    }, 
                    "MW2065": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道2-扫码失败"
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
                        "desc": "设备伺服报警，请检查伺服驱动器的报错代码"
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
                        "desc": " 轨道A扫码位置读卡超时！"
                    }, 
                    "MW2101": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " 轨道B扫码位置读卡超时！"
                    }, 
                    "MW2102": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event102"
                    }, 
                    "MW2103": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event103"
                    }, 
                    "MW2104": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event104"
                    }, 
                    "MW2105": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event105"
                    }, 
                    "MW2106": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event106"
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
                        "desc": " Event110"
                    }, 
                    "MW2111": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event111"
                    }, 
                    "MW2112": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event112"
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
                        "desc": " Event130"
                    }, 
                    "MW2131": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event131"
                    }, 
                    "MW2132": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": " Event132"
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
                    }
                }, 
                ("D05", "MP18", "MP-TJ-GLU-040"): {
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
                        "desc": "工位-1-擦胶枪夹紧气缸感应异常--请检查X4-X5-Y4-Y5的线路及点位！"
                    }, 
                    "MW2041": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-2-擦胶枪夹紧气缸感应异常--请检查X6-X7-Y6-Y7的线路及点位！"
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
                        "desc": "Event65"
                    }, 
                    "MW2066": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event66"
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
                        "desc": "副轨道A缓冲阻挡器2放行超时，请检查，点动复位清除报警！"
                    }, 
                    "MW2133": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "副轨道B缓冲阻挡器2放行超时，请检查，点动复位清除报警！"
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
                        "desc": "工位-1-胶桶1缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2141": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-1-胶桶2缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2142": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-1-胶桶3缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2143": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-1-胶桶4缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2144": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "Event144"
                    }, 
                    "MW2145": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-2-胶桶1缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2146": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-2-胶桶2缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2147": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-2-胶桶3缺胶报警，请检查并及时换胶！"
                    }, 
                    "MW2148": {
                        "alias": "", 
                        "tag": 1, 
                        "desc": "工位-2-胶桶4缺胶报警，请检查并及时换胶！"
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
                }
}
