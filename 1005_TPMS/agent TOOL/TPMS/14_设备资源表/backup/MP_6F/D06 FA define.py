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
                    "desc": "??????A?????????????????????????????????"
                }, 
                "D2001": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B?????????????????????????????????"
                }, 
                "D2002": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A???????????????????????????"
                }, 
                "D2003": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B???????????????????????????"
                }, 
                "D2004": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A?????????????????????"
                }, 
                "D2005": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B?????????????????????"
                }, 
                "D2006": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????????????????"
                }, 
                "D2007": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B?????????????????????????????????"
                }, 
                "D2008": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????"
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
                    "desc": "????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
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
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": "?????????????????????????????????????????????????????????????????????"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????????????????????????????????????????????????????????????????"
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
                    "desc": "????????????????????????????????????????????????????????????"
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
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1??????????????????????????????IO ??????X32 ??????X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1??????????????????????????????IO ??????X45 ??????X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2??????????????????????????????IO ??????X62 ??????X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2??????????????????????????????IO ??????X75 ??????X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????????????????"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????????????????"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????????????????????????????????????????"
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
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A?????????????????????????????????IO ??????X220 ??????X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B?????????????????????????????????IO ??????X226 ??????X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A????????????????????????"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B????????????????????????"
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
                    "desc": "??????A???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
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
                    "desc": "??????1?????????????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2?????????????????????????????????"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????3?????????????????????????????????"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????4?????????????????????????????????"
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
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A????????????????????????X34X36???????????????X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B????????????????????????????????????X50X52???????????????X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A????????????????????????X64X66???????????????X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B????????????????????????X80X82???????????????X77X81"
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
                    "desc": " ????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
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
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": " ??????A????????????????????????????????????Y21???X31"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????????????????????????????Y22???X32"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????????????????????????????X31???X32"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????????????????????????????Y25???X35"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????????????????????????????Y26???X36"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????????????????????????????X35???X36"
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
                    "desc": " ??????A????????????????????????"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????????????????"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????1????????????????????????????????????"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????2????????????????????????????????????"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????1??????????????????"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????1??????????????????"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????2??????????????????"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????2??????????????????"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????????????????????????????"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ????????????????????????????????????????????????Y17??????????????????_x000D_\n?????????????????????????????????"
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
                    "desc": " ??????A??????-1-X-?????????????????????????????????1CM???_x000D_\n????????????????????????X??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????-2-X-?????????????????????????????????1CM???_x000D_\n????????????????????????X??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????-1-Y-?????????????????????????????????1CM???_x000D_\n????????????????????????Y??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????-2-Y-?????????????????????????????????1CM???_x000D_\n????????????????????????Y??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event134"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-1-X-?????????????????????????????????1CM???_x000D_\n????????????????????????X??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-2-X-?????????????????????????????????1CM???_x000D_\n????????????????????????X??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-1-Y-?????????????????????????????????1CM???_x000D_\n????????????????????????Y??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-2-Y-?????????????????????????????????1CM???_x000D_\n????????????????????????Y??????????????????1CM???_x000D_\n??????????????????????????????????????????"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event139"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????-1-??????R1-R2??????????????????30??????_x000D_\n?????????R????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????-2-??????R1-R2??????????????????30??????_x000D_\n?????????R????????????????????????"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-1-??????R1-R2??????????????????30??????_x000D_\n?????????R????????????????????????"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????-2-??????R1-R2??????????????????30??????_x000D_\n?????????R????????????????????????"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " Event144"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ????????????????????????????????????X-Y???????????????????????????1.5CM,_x000D_\n????????????????????????????????????????????????????????????????????????????????????????????????"
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
                    "desc": " ????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????????????????_x000D_\n????????????????????????????????????????????????"
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
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": " ????????????????????????????????????????????????????????????"
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
                    "desc": " ??????A?????????????????????????????????????????????????????????X32???????????????Y32???"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X33???????????????Y33???"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X32?????????X33???"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X34 X36???????????????Y34???"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X35 X37???????????????Y35???"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????X35 X37 X34 X36???"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????????????????????????????X40 X42???????????????Y36???"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????????????????????????????X41 X43???????????????Y37???"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????????????????X41 X42 X43 X40???"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A??????????????????????????????????????????"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X45???????????????Y41???"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X46???????????????Y42???"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X45?????????X46???"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X47 X51???????????????Y43???"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X50 X52???????????????Y44???"
                }, 
                "MW2116": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????X47 X50 X51 X52???"
                }, 
                "MW2117": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????????????????X53 X55???????????????Y45???"
                }, 
                "MW2118": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????????????????X54 X56???????????????Y46???"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????????????????X53 X54 X55 X56???"
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
                    "desc": " ??????A???????????????????????????????????????????????????????????????X71 X73???????????????Y55???"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????????????????X70 X72???????????????Y54???"
                }, 
                "MW2133": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X70 X71 X72 X73???"
                }, 
                "MW2134": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????????????????X74 X75???????????????Y57???"
                }, 
                "MW2135": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????????????????????????????X74 X75???????????????Y56???"
                }, 
                "MW2136": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????????????????X74 X75???"
                }, 
                "MW2137": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????PCB?????????????????????????????????????????????X76 X77???????????????Y61???"
                }, 
                "MW2138": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????PCB?????????????????????????????????????????????X76 X77???????????????Y60???"
                }, 
                "MW2139": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????PCB???????????????????????????????????????X76 X77???"
                }, 
                "MW2140": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B??????????????????????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????X81 X83???????????????Y65???"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????X80 X82???????????????Y64???"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X80 X81 X82 X83???"
                }, 
                "MW2144": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????X84 X85???????????????Y67???"
                }, 
                "MW2145": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????????????????????????????X84 X85???????????????Y66???"
                }, 
                "MW2146": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????????????????X84 X85???"
                }, 
                "MW2147": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????PCB?????????????????????????????????????????????X86 X87???????????????Y71???"
                }, 
                "MW2148": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????PCB?????????????????????????????????????????????X86 X87???????????????Y80???"
                }, 
                "MW2149": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????PCB???????????????????????????????????????X86 X87???"
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
                    "desc": "????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
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
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": "?????????????????????????????????????????????????????????????????????"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????????????????????????????????????????????????????????????????"
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
                    "desc": "????????????????????????????????????????????????????????????"
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
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1??????????????????????????????IO ??????X32 ??????X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1??????????????????????????????IO ??????X45 ??????X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2??????????????????????????????IO ??????X62 ??????X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2??????????????????????????????IO ??????X75 ??????X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????????????????"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????????????????"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????????????????????????????????????????"
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
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A?????????????????????????????????IO ??????X220 ??????X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B?????????????????????????????????IO ??????X226 ??????X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A????????????????????????"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B????????????????????????"
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
                    "desc": "??????A???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
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
                    "desc": "??????1?????????????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2?????????????????????????????????"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????3?????????????????????????????????"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????4?????????????????????????????????"
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
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A????????????????????????X34X36???????????????X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B????????????????????????????????????X50X52???????????????X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A????????????????????????X64X66???????????????X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B????????????????????????X80X82???????????????X77X81"
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
                    "desc": "????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
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
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": "?????????????????????????????????????????????????????????????????????"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????????????????????????????????????????????????????????????????"
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
                    "desc": "????????????????????????????????????????????????????????????"
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
                    "desc": "?????????????????????????????????"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1??????????????????????????????IO ??????X32 ??????X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1??????????????????????????????IO ??????X45 ??????X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2??????????????????????????????IO ??????X62 ??????X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2??????????????????????????????IO ??????X75 ??????X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????????????????"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????????????????"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????????????????????????????????????????"
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
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A?????????????????????????????????IO ??????X220 ??????X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B?????????????????????????????????IO ??????X226 ??????X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A????????????????????????"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B????????????????????????"
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
                    "desc": "??????A???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
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
                    "desc": "??????1???????????????????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2???????????????????????????????????????"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????3???????????????????????????????????????"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????4???????????????????????????????????????"
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
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A????????????????????????X34X36???????????????X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B????????????????????????????????????X50X52???????????????X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A????????????????????????X64X66???????????????X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B????????????????????????X80X82???????????????X77X81"
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
                    "desc": "????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
                }, 
                "MW2052": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????_x000D_\n???????????????"
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
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": "?????????????????????????????????????????????????????????????????????"
                }, 
                "MW2066": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????????????????????????????????????????????????????????????????????????????"
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
                    "desc": "????????????????????????????????????????????????????????????"
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
                    "desc": "?????????????????????????????????"
                }, 
                "MW2101": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1????????????????????????????????????IO ??????X32 ??????X33 ??????Y32 ??????Y33"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????1??????????????????????????????IO ??????X32 ??????X33"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1????????????????????????????????????IO ??????X45 ??????X46 ??????Y41 ??????Y42"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????1??????????????????????????????IO ??????X45 ??????X46"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2????????????????????????????????????IO ??????X62 ??????X63 ??????Y61 ??????Y62"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????2??????????????????????????????IO ??????X62 ??????X63"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2????????????????????????????????????IO ??????X75 ??????X76 ??????Y70 ??????Y71"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????2??????????????????????????????IO ??????X75 ??????X76"
                }, 
                "MW2113": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????A??????????????????"
                }, 
                "MW2114": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B??????????????????"
                }, 
                "MW2115": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "????????????????????????????????????????????????"
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
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2119": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A???????????????????????????????????????IO ??????X220 ??????X221 ??????Y220 ??????Y221"
                }, 
                "MW2120": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A?????????????????????????????????IO ??????X220 ??????X221"
                }, 
                "MW2121": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B???????????????????????????????????????IO ??????X226 ??????X227 ??????Y226 ??????Y227"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B?????????????????????????????????IO ??????X226 ??????X227"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????A????????????????????????"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "???????????????B????????????????????????"
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
                    "desc": "??????A???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????B???????????????????????????????????????_x000D_\n?????????????????????????????????????????????????????????"
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
                    "desc": "??????1???????????????????????????????????????"
                }, 
                "MW2141": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2???????????????????????????????????????"
                }, 
                "MW2142": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????3???????????????????????????????????????"
                }, 
                "MW2143": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????4???????????????????????????????????????"
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
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2151": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A???????????????????????????????????????X34X36???????????????X35X37?????????Y35??????Y34"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????A????????????????????????X34X36???????????????X35X37"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B???????????????????????????????????????X50X52???????????????X47X51?????????Y35??????Y34"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????1??????B????????????????????????????????????X50X52???????????????X47X51"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A???????????????????????????????????????X64X66???????????????X65X67?????????Y64??????Y63"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????A????????????????????????X64X66???????????????X65X67"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B???????????????????????????????????????X80X82???????????????X77X81?????????Y73??????Y72"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": "??????2??????B????????????????????????X80X82???????????????X77X81"
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
                    "desc": " ????????????????????????????????????_x000D_\n????????????????????????????????????????????????"
                }, 
                "MW2051": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ?????????????????????????????????_x000D_\n????????????????????????????????????????????????"
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
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2058": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ????????????PLC????????????????????????????????????_x000D_\n??????????????????PLC???????????????????????????-????????????????????????_x000D_\n???????????????PLC??????????????????"
                }, 
                "MW2059": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???PC????????????????????????????????????_x000D_\n?????????PC???????????????????????????-????????????????????????_x000D_\n??????PC??????????????????"
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
                    "desc": " ????????????????????????????????????????????????????????????"
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
                    "desc": " ??????A????????????????????????????????????X30?????????Y20???????????????????????????"
                }, 
                "MW2102": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????????????????????????????X31?????????Y21???????????????????????????"
                }, 
                "MW2103": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????X30 X31"
                }, 
                "MW2104": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????X34?????????Y24???????????????????????????"
                }, 
                "MW2105": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????X35?????????Y25???????????????????????????"
                }, 
                "MW2106": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A????????????????????????????????????X34 X35"
                }, 
                "MW2107": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????X36 X40 ??? ??????Y26???????????????????????????"
                }, 
                "MW2108": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????X37 X41?????????Y27???????????????????????????"
                }, 
                "MW2109": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A?????????????????????????????????????????????X36 X37 X40 X41???"
                }, 
                "MW2110": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????X42 X44?????????Y30???????????????????????????"
                }, 
                "MW2111": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????????X43 X45?????????Y31???????????????????????????"
                }, 
                "MW2112": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????A???????????????????????????????????? X42 X43 X44 X45"
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
                    "desc": " ??????B????????????????????????????????????X50?????????Y34???????????????????????????"
                }, 
                "MW2122": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????????????????????????????X51?????????Y35???????????????????????????"
                }, 
                "MW2123": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????X50 X51"
                }, 
                "MW2124": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????X54?????????Y40???????????????????????????"
                }, 
                "MW2125": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????X55?????????Y41???????????????????????????"
                }, 
                "MW2126": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B????????????????????????????????????X54 X55"
                }, 
                "MW2127": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????X56 X60 ??? ??????Y42???????????????????????????"
                }, 
                "MW2128": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????X57 X61?????????Y43???????????????????????????"
                }, 
                "MW2129": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B?????????????????????????????????????????????X56 X57 X60 X61???"
                }, 
                "MW2130": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????X62 X64?????????Y44???????????????????????????"
                }, 
                "MW2131": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????????X63 X65?????????Y45???????????????????????????"
                }, 
                "MW2132": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????????????? X62 X63 X64 X65"
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
                    "desc": " ???????????????????????????1???????????????????????????X61?????????Y60??????????????????????????????"
                }, 
                "MW2152": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????1???????????????????????????X61?????????Y60??????????????????????????????"
                }, 
                "MW2153": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????1?????????????????????"
                }, 
                "MW2154": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????2???????????????????????????X62?????????Y62??????????????????????????????"
                }, 
                "MW2155": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????2???????????????????????????X62?????????Y62??????????????????????????????"
                }, 
                "MW2156": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????2?????????????????????"
                }, 
                "MW2157": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????3???????????????????????????X65?????????Y65??????????????????????????????"
                }, 
                "MW2158": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????3???????????????????????????X65?????????Y64??????????????????????????????"
                }, 
                "MW2159": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????3?????????????????????"
                }, 
                "MW2160": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????4???????????????????????????X67?????????Y67??????????????????????????????"
                }, 
                "MW2161": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????4???????????????????????????X67?????????Y66??????????????????????????????"
                }, 
                "MW2162": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ???????????????????????????4?????????????????????"
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
                    "desc": " ??????A???????????????????????????"
                }, 
                "MW2175": {
                    "alias": "", 
                    "tag": 1, 
                    "desc": " ??????B???????????????????????????"
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
