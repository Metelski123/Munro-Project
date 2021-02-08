import pdb
from models.munro import Munro
from models.climber import Climber
from models.bag import Bag

import repositories.munro_repository as munro_repository
import repositories.climber_repository as climber_repository
import repositories.bag_repository as bag_repository

bag_repository.delete_all()
munro_repository.delete_all()
climber_repository.delete_all()

climber1 = Climber('Janek Metelski')
climber_repository.save(climber1)

climber2 = Climber('Jessica Metelski')
climber_repository.save(climber2)

climber3 = Climber('Jimmy Saville')
climber_repository.save(climber3)

munro1 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro2 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro3 = Munro('Braeriach', 1296)
munro_repository.save(munro1)

munro4 = Munro('Cairn Toul', 1261)
munro_repository.save(munro2)

munro5 = Munro('Sgor an Lochain Uaine', 1258)
munro_repository.save(munro1)

munro6 = Munro('Cairn Gorm', 1245)
munro_repository.save(munro2)

munro7 = Munro('Aonach Beag', 1234)
munro_repository.save(munro1)

munro8 = Munro('Aonach Mor', 1221)
munro_repository.save(munro2)

munro9 = Munro('Carn Mor Dearg', 1220)
munro_repository.save(munro1)

munro10 = Munro('Ben Lawers', 1214)
munro_repository.save(munro2)

munro11 = Munro('Beinn a Bhuird', 1197)
munro_repository.save(munro1)

munro12 = Munro('Carn Eige', 1183)
munro_repository.save(munro2)

munro13 = Munro('Beinn Mheadhoin', 1182)
munro_repository.save(munro1)

munro14 = Munro('Mam Sodhail', 1181)
munro_repository.save(munro2)

munro15 = Munro('Stob Choire Claurigh', 1177)
munro_repository.save(munro1)

munro16 = Munro('Ben More', 1174)
munro_repository.save(munro2)

munro17 = Munro('Ben Avon', 1171)
munro_repository.save(munro1)

munro18 = Munro('Stob Binnein', 1165)
munro_repository.save(munro2)

munro19 = Munro('Beinn Bhrotain', 1157)
munro_repository.save(munro1)

munro20 = Munro('Derry Cairngorm', 1309)
munro_repository.save(munro2)

munro21 = Munro('Lochnagar', 1155)
munro_repository.save(munro1)

munro22 = Munro('gurr nan Ceathreamhnan', 1151)
munro_repository.save(munro2)

munro23 = Munro('Bidean nam Bian', 1150)
munro_repository.save(munro1)

munro24 = Munro('Sgurr na Lapaich', 1150)
munro_repository.save(munro2)

munro25 = Munro('Ben Alder', 1148)
munro_repository.save(munro1)

munro26 = Munro('Geal Charn Alder', 1132)
munro_repository.save(munro2)

munro27 = Munro('Ben Lui', 1130)
munro_repository.save(munro1)

munro28 = Munro('Binnein Mor', 1130)
munro_repository.save(munro2)

munro29 = Munro('Creag Meagaidh', 1330)
munro_repository.save(munro1)

munro30 = Munro('An Riabhachan', 1129)
munro_repository.save(munro2)

munro31 = Munro('Ben Cruachan', 1126)
munro_repository.save(munro1)

munro32 = Munro('Carn nan Gabhar', 1121)
munro_repository.save(munro2)

munro33 = Munro('A-Chralaig', 1120)
munro_repository.save(munro1)

munro34 = Munro('An Stuc', 1118)
munro_repository.save(munro2)

munro35 = Munro('Carn a-Choire Bhoidheach', 1118)
munro_repository.save(munro1)

munro36 = Munro('Meall Garbh- Ben Lawers', 1118)
munro_repository.save(munro2)

munro37 = Munro('Sgor Gaoith', 1118)
munro_repository.save(munro1)

munro38 = Munro('Aonach Beag - Alder', 1116)
munro_repository.save(munro2)

munro39 = Munro('Stob Coire an Laoigh', 1116)
munro_repository.save(munro1)

munro40 = Munro('Stob Coire Easain', 1115)
munro_repository.save(munro2)

munro41 = Munro('Monadh Mor', 1113)
munro_repository.save(munro1)

munro42 = Munro('Tom a-Choinich', 1112)
munro_repository.save(munro2)

munro43 = Munro('Sgurr Mor', 1110)
munro_repository.save(munro1)

munro44 = Munro('Sgurr nan Conbhairean', 1109)
munro_repository.save(munro2)

munro45 = Munro('Meall a-Bhuiridh', 1108)
munro_repository.save(munro1)

munro46 = Munro('Stoba-Choire Mheadhoin', 1106)
munro_repository.save(munro2)

munro47 = Munro('Beinn Ghlas', 1103)
munro_repository.save(munro1)

munro48 = Munro('Beinn Eibhinn', 1102)
munro_repository.save(munro2)

munro49 = Munro('Mullach Fraoch-choire', 1102)
munro_repository.save(munro1)

munro50 = Munro('Creise', 1100)
munro_repository.save(munro2)

munro51 = Munro('Sgurr a-Mhaim', 1099)
munro_repository.save(munro1)

munro52 = Munro('Sgurr Choinnich Mor', 1094)
munro_repository.save(munro2)

munro53 = Munro('Sgurr nan Clach Geala', 1093)
munro_repository.save(munro1)

munro54 = Munro('Bynack More', 1090)
munro_repository.save(munro2)

munro55 = Munro('Stob Ghabhar', 1090)
munro_repository.save(munro1)

munro56 = Munro('Beinn a-Chlachair', 1087)
munro_repository.save(munro2)

munro57 = Munro('Beinn Dearg - Ullapool', 1084)
munro_repository.save(munro1)

munro58 = Munro('Schiehallion', 1083)
munro_repository.save(munro2)

munro59 = Munro('Sgurr a-Choire Ghlais', 1083)
munro_repository.save(munro1)

munro60 = Munro('Beinn a Chaorainn - Cairngorms', 1082)
munro_repository.save(munro2)

munro61 = Munro('Beinn a-Chreachain', 1082)
munro_repository.save(munro1)

munro62 = Munro('Beinn Heasgarnich', 1078)
munro_repository.save(munro2)

munro63 = Munro('Ben Starav', 1078)
munro_repository.save(munro1)

munro64 = Munro('Beinn Dorain', 1076)
munro_repository.save(munro2)

munro65 = Munro('Stob Coire Sgreamhach', 1072)
munro_repository.save(munro1)

munro66 = Munro('Braigh Coire Chruinn-bhalgain', 1070)
munro_repository.save(munro2)

munro67 = Munro('An Socach - Mullardoch', 1069)
munro_repository.save(munro1)

munro68 = Munro('Meall Corranaich', 1069)
munro_repository.save(munro2)

munro69 = Munro('Glas Maol', 1068)
munro_repository.save(munro1)

munro70 = Munro('Sgurr Fhuaran', 1067)
munro_repository.save(munro2)

munro71 = Munro('Cairn of Claise', 1064)
munro_repository.save(munro1)

munro72 = Munro('Bidein a-Ghlas Thuill - An Teallach', 1062)
munro_repository.save(munro2)

munro73 = Munro('Sgurr Fiona - An Teallach', 1060)
munro_repository.save(munro1)

munro74 = Munro('Na Gruagaichean', 1056)
munro_repository.save(munro2)

munro75 = Munro('Spidean a-Choire Leith - Liathach', 1055)
munro_repository.save(munro1)

munro76 = Munro('Stob Poite Coire Ardair', 1054)
munro_repository.save(munro2)

munro77 = Munro('Toll Creagach', 1054)
munro_repository.save(munro1)

munro78 = Munro('Sgurr a-Chaorachain', 1053)
munro_repository.save(munro2)

munro79 = Munro('Glas Tulaichean', 1051)
munro_repository.save(munro1)

munro80 = Munro('Beinn a-Chaorainn - Glen Spean', 1050)
munro_repository.save(munro2)

munro81 = Munro('Geal Charn', 1049)
munro_repository.save(munro1)

munro82 = Munro('Sgurr Fhuar-thuill', 1049)
munro_repository.save(munro82)

munro83 = Munro('Carn an t-Sagairt Mor', 1047)
munro_repository.save(munro83)

munro84 = Munro('Creag Mhor - Glen Lochay', 1047)
munro_repository.save(munro84)

munro85 = Munro('Ben Wyvis', 1046)
munro_repository.save(munro85)

munro86 = Munro('Chno Dearg', 1046)
munro_repository.save(munro86)

munro87 = Munro('Cruach Ardrain', 1046)
munro_repository.save(munro87)

munro88 = Munro('Beinn lutharn Mhor', 1045)
munro_repository.save(munro88)

munro89 = Munro('Meall nan Tarmachan', 1044)
munro_repository.save(munro89)

munro90 = Munro('Stob Coir an Albannaich', 1044)
munro_repository.save(munro90)

munro91 = Munro('Carn Mairg', 1042)
munro_repository.save(munro91)

munro92 = Munro('Sgurr na Ciche', 1040)
munro_repository.save(munro92)

munro93 = Munro('Meall Ghaordaidh', 1039)
munro_repository.save(munro93)

munro94 = Munro('Beinn Achaladair', 1038)
munro_repository.save(munro94)

munro95 = Munro('Carn a-Mhaim', 1037)
munro_repository.save(munro95)

munro96 = Munro('Sgurr a-Bhealaich Dheirg', 1036)
munro_repository.save(munro96)

munro97 = Munro('Gleouraich', 1035)
munro_repository.save(munro97)

munro98 = Munro('Carn Dearg - Loch Pattack', 1034)
munro_repository.save(munro98)

munro99 = Munro('Am Bodach', 1032)
munro_repository.save(munro99)

munro100 = Munro('Beinn Fhada', 1032)
munro_repository.save(munro100)

munro101 = Munro('Ben Oss', 1029)
munro_repository.save(munro101)

munro102 = Munro('Carn an Righ', 1029)
munro_repository.save(munro102)

munro103 = Munro('Carn Gorm', 1029)
munro_repository.save(munro103)

munro104 = Munro('Sgurr a-Mhaoraich', 1027)
munro_repository.save(munro104)

munro105 = Munro('Sgurr na Ciste Duibhe', 1027)
munro_repository.save(munro105)

munro106 = Munro('Ben Challum', 1025)
munro_repository.save(munro106)

munro107 = Munro('Sgorr Dhearg - Beinn a-Bheithir', 1024)
munro_repository.save(munro107)

munro108 = Munro('Mullach an Rathain - Liathach', 1023)
munro_repository.save(munro108)

munro109 = Munro('Aonach Air Chrith', 1021)
munro_repository.save(munro109)

munro110 = Munro('Stob Dearg - Buachaille Etive Mor', 1021)
munro_repository.save(munro110)

munro111 = Munro('Ladhar Bheinn', 1020)
munro_repository.save(munro111)

munro112 = Munro('Beinn Bheoil', 1019)
munro_repository.save(munro112)

munro113 = Munro('Carn an Tuirc', 1019)
munro_repository.save(munro113)

munro114 = Munro('Mullach Clach a-Bhlair', 1019)
munro_repository.save(munro114)

munro115 = Munro('Mullach Coire Mhic Fhearchair', 1019)
munro_repository.save(munro115)

munro116 = Munro('Garbh Chioch Mhor', 1013)
munro_repository.save(munro116)

munro117 = Munro('Cairn Bannoch', 1012)
munro_repository.save(munro117)

munro118 = Munro('Beinn Ime', 1011)
munro_repository.save(munro118)

munro119 = Munro('Beinn Udlamain', 1010)
munro_repository.save(munro119)

munro120 = Munro('Ruadh-stac Mor - Beinn Eighe', 1010)
munro_repository.save(munro120)

munro121 = Munro('Sgurr an Doire Leathain', 1010)
munro_repository.save(munro121)

munro122 = Munro('Sgurr Eilde Mor', 1010)
munro_repository.save(munro122)

munro123 = Munro('The Saddle', 1010)
munro_repository.save(munro123)

munro124 = Munro('Beinn Dearg - Blair Atholl', 1008)
munro_repository.save(munro124)

munro125 = Munro('Maoile Lunndaidh', 1007)
munro_repository.save(munro125)

munro126 = Munro('An Sgarsoch', 1006)
munro_repository.save(munro127)

munro127 = Munro('Carn Liath - Creag Meagaidh', 1006)
munro_repository.save(munro127)

munro128 = Munro('Beinn Fhionnlaidh - Carn Eige', 1005)
munro_repository.save(munro128)

munro129 = Munro('Beinn an Dothaidh', 1004)
munro_repository.save(munro129)

munro130 = Munro('Sgurr an Lochain', 1004)
munro_repository.save(munro130)

munro131 = Munro('The Devils Point', 1004)
munro_repository.save(munro131)

munro132 = Munro('Sgurr Mor - Loch Quoich', 1003)
munro_repository.save(munro132)

munro133 = Munro('Sail Chaorainn', 1002)
munro_repository.save(munro133)

munro134 = Munro('Sgurr na Carnach', 1002)
munro_repository.save(munro134)

munro135 = Munro('Aonach Meadhoin', 1001)
munro_repository.save(munro135)

munro136 = Munro('Meall Greigh', 1001)
munro_repository.save(munro136)

munro137 = Munro('Sgorr Dhonuill - Beinn a-Bheithir', 1001)
munro_repository.save(munro137)

munro138 = Munro('Sgurr Breac', 999)
munro_repository.save(munro138)

munro139 = Munro('Sgurr Choinnich', 999)
munro_repository.save(munro139)

munro140 = Munro('Stob Ban - Mamores', 999)
munro_repository.save(munro140)

munro141 = Munro('Ben More Assynt', 998)
munro_repository.save(munro141)

munro142 = Munro('Broad Cairn', 998)
munro_repository.save(munro142)

munro143 = Munro('Stob Daimh', 998)
munro_repository.save(munro143)

munro144 = Munro('A-Chailleach', 997)
munro_repository.save(munro144)

munro145 = Munro('Glas Bheinn Mhor', 997)
munro_repository.save(munro145)

munro146 = Munro('Spidean Mialach', 996)
munro_repository.save(munro146)

munro147 = Munro('An Caisteal', 995)
munro_repository.save(munro147)

munro148 = Munro('Carn an Fhidhleir - Carn Ealar', 994)
munro_repository.save(munro148)

munro149 = Munro('Sgor na h-Ulaidh', 994)
munro_repository.save(munro149)

munro150 = Munro('Sgurr na Ruaidhe', 993)
munro_repository.save(munro150)

munro151 = Munro('Spidean Coire nan Clach - Beinn Eighe', 993)
munro_repository.save(munro151)

munro152 = Munro('Carn nan Gobhar - Loch Mullardoch', 992)
munro_repository.save(munro152)

munro153 = Munro('Carn nan Gobhar - Strathfarrar', 992)
munro_repository.save(munro153)

munro154 = Munro('Sgurr Alasdair', 992)
munro_repository.save(munro154)

munro155 = Munro('Sgairneach Mhor', 991)
munro_repository.save(munro155)

munro156 = Munro('Beinn Eunaich', 989)
munro_repository.save(munro156)

munro157 = Munro('Sgurr Ban', 989)
munro_repository.save(munro157)

munro158 = Munro('Conival', 987)
munro_repository.save(munro158)

munro159 = Munro('Creag Leacach', 987)
munro_repository.save(munro159)

munro160 = Munro('Druim Shionnach', 987)
munro_repository.save(munro160)

munro161 = Munro('Gulvain', 987)
munro_repository.save(munro161)

munro162 = Munro('Inaccessible Pinnacle', 986)
munro_repository.save(munro162)

munro163 = Munro('Lurg Mhor', 986)
munro_repository.save(munro163)

munro164 = Munro('Sgurr Mor - Beinn Alligin', 986)
munro_repository.save(munro164)

munro165 = Munro('Ben Vorlich - Loch Earn', 985)
munro_repository.save(munro165)

munro166 = Munro('An Gearanach', 982)
munro_repository.save(munro166)

munro167 = Munro('Mullach na Dheiragain', 982)
munro_repository.save(munro167)

munro168 = Munro('Creag Mhor - Meall na Aighean', 981)
munro_repository.save(munro168)

munro169 = Munro('Maol chinn-dearg', 981)
munro_repository.save(munro169)

munro170 = Munro('Slioch', 981)
munro_repository.save(munro170)

munro171 = Munro('Stob Coire a-Chairn', 981)
munro_repository.save(munro171)

munro172 = Munro('Beinn a-Chochuill', 980)
munro_repository.save(munro172)

munro173 = Munro('Ciste Dhubh', 979)
munro_repository.save(munro173)

munro174 = Munro('Stob Coire Sgriodain', 979)
munro_repository.save(munro174)

munro175 = Munro('Beinn Dubhchraig', 978)
munro_repository.save(munro175)

munro176 = Munro('Cona Mheall', 978)
munro_repository.save(munro176)

munro177 = Munro('Meall nan Ceapraichean', 977)
munro_repository.save(munro177)

munro178 = Munro('Stob Ban - Grey Corries', 977)
munro_repository.save(munro178)

munro179 = Munro('A-Mharconaich', 975)
munro_repository.save(munro179)

munro180 = Munro('Carn a-Gheoidh', 975)
munro_repository.save(munro180)

munro181 = Munro('Carn Liath - Beinn a Ghlo', 975)
munro_repository.save(munro181)

munro182 = Munro('Stuc a-Chroin', 975)
munro_repository.save(munro182)

munro183 = Munro('Beinn Sgritheall', 974)
munro_repository.save(munro183)

munro184 = Munro('Ben Lomond', 974)
munro_repository.save(munro184)

munro185 = Munro('Sgurr a-Ghreadaidh', 973)
munro_repository.save(munro185)

munro186 = Munro('Meall Garbh - Carn Mairg', 968)
munro_repository.save(munro186)

munro187 = Munro('A-Mhaighdean', 967)
munro_repository.save(munro187)

munro188 = Munro('Sgorr nam Fiannaidh - Aonach Eagach', 967)
munro_repository.save(munro188)

munro189 = Munro('Ben More - Mull', 966)
munro_repository.save(munro189)

munro190 = Munro('Sgurr na Banachdich', 965)
munro_repository.save(munro190)

munro191 = Munro('Sgurr nan Gillean', 964)
munro_repository.save(munro191)

munro192 = Munro('Carn a-Chlamain', 963)
munro_repository.save(munro192)

munro193 = Munro('Sgurr Thuilm', 963)
munro_repository.save(munro193)

munro194 = Munro('Sgorr Ruadh', 962)
munro_repository.save(munro194)

munro195 = Munro('Ben Klibreck', 961)
munro_repository.save(munro195)

munro196 = Munro('Beinn nan Aighenan', 960)
munro_repository.save(munro196)

munro197 = Munro('Stuchd an Lochain', 960)
munro_repository.save(munro197)

munro198 = Munro('Beinn Fhionnlaidh', 959)
munro_repository.save(munro198)

munro199 = Munro('Meall Glas', 959)
munro_repository.save(munro199)

munro200 = Munro('Bruach na Frithe', 958)
munro_repository.save(munro200)

munro201 = Munro('Tolmount', 958)
munro_repository.save(munro201)

munro202 = Munro('Carn Ghluasaid', 957)
munro_repository.save(munro202)

munro203 = Munro('Tom Buidhe', 957)
munro_repository.save(munro203)

munro204 = Munro('Saileag', 956)
munro_repository.save(munro204)

munro205 = Munro('Sgurr nan Coireachan - Glenfinnan', 956)
munro_repository.save(munro205)

munro206 = Munro('Stob Dubh - Buachaille Etive Beag', 956)
munro_repository.save(munro206)

munro207 = Munro('Stob na Broige - Buachaille Etive Mor', 956)
munro_repository.save(munro207)

munro208 = Munro('Sgor Gaibhre', 955)
munro_repository.save(munro208)

munro209 = Munro('Am Faochagach', 954)
munro_repository.save(munro209)

munro210 = Munro('Beinn Liath Mhor Fannaich', 954)
munro_repository.save(munro210)

munro211 = Munro('Beinn Mhanach', 953)
munro_repository.save(munro211)

munro212 = Munro('Meall Dearg - Aonach Eagach', 953)
munro_repository.save(munro212)

munro213 = Munro('Sgurr nan Coireachan - Glen Dessary', 953)
munro_repository.save(munro213)

munro214 = Munro('Meall Chuaich', 951)
munro_repository.save(munro214)

munro215 = Munro('Meall Gorm', 949)
munro_repository.save(munro215)

munro216 = Munro('Beinn Bhuidhe', 948)
munro_repository.save(munro216)

munro217 = Munro('Sgurr Mhic Choinnich', 948)
munro_repository.save(munro217)

munro218 = Munro('Creag a-Mhaim', 947)
munro_repository.save(munro218)

munro219 = Munro('Driesh', 947)
munro_repository.save(munro219)

munro220 = Munro('Beinn Tulaichean', 946)
munro_repository.save(munro220)

munro221 = Munro('Carn Bhac', 946)
munro_repository.save(munro221)

munro222 = Munro('Meall Buidhe - Knoydart', 946)
munro_repository.save(munro222)

munro223 = Munro('Bidein a-Choire Sheasgaich', 945)
munro_repository.save(munro223)

munro224 = Munro('Carn Dearg - Monadhliath', 945)
munro_repository.save(munro224)

munro225 = Munro('Sgurr na Sgine', 945)
munro_repository.save(munro225)

munro226 = Munro('Stob a-Choire Odhair', 945)
munro_repository.save(munro226)

munro227 = Munro('An Socach - Braemar', 944)
munro_repository.save(munro227)

munro228 = Munro('Sgurr Dubh Mor', 944)
munro_repository.save(munro228)

munro229 = Munro('Ben Vorlich - Loch Lomond', 943)
munro_repository.save(munro229)

munro230 = Munro('Binnein Beag', 943)
munro_repository.save(munro230)

munro231 = Munro('Beinn a-Chroin', 942)
munro_repository.save(munro231)

munro232 = Munro('Carn Dearg - Corrour', 941)
munro_repository.save(munro232)

munro233 = Munro('Carn na Caim', 941)
munro_repository.save(munro233)

munro234 = Munro('Luinne Bheinn', 939)
munro_repository.save(munro234)

munro235 = Munro('Mount Keen', 939)
munro_repository.save(munro235)

munro236 = Munro('Mullach nan Coirean', 939)
munro_repository.save(munro236)

munro237 = Munro('Beinn na Lap', 937)
munro_repository.save(munro237)

munro238 = Munro('Beinn Sgulaird', 937)
munro_repository.save(munro238)

munro239 = Munro('Beinn Tarsuinn', 937)
munro_repository.save(munro239)

munro240 = Munro('Sron a-Choire Ghairbh', 937)
munro_repository.save(munro240)

munro241 = Munro('A-Bhuidheanach Bheag', 936)
munro_repository.save(munro241)

munro242 = Munro('Am Basteir', 934)
munro_repository.save(munro242)

munro243 = Munro('Meall a-Chrasgaidh', 934)
munro_repository.save(munro243)

munro244 = Munro('Beinn Chabhair', 933)
munro_repository.save(munro244)

munro245 = Munro('Fionn Bheinn', 933)
munro_repository.save(munro245)

munro246 = Munro('Maol Chean-dearg', 933)
munro_repository.save(munro246)

munro247 = Munro('The Cairnwell', 933)
munro_repository.save(munro247)

munro248 = Munro('Meall Buidhe - Glen Lyon', 932)
munro_repository.save(munro248)

munro249 = Munro('Beinn Bhreac', 931)
munro_repository.save(munro249)

munro250 = Munro('Ben Chonzie', 931)
munro_repository.save(munro250)

munro251 = Munro('A-Chailleach - Monadhliath', 930)
munro_repository.save(munro251)

munro252 = Munro('Bla Bheinn', 928)
munro_repository.save(munro252)

munro253 = Munro('Mayar', 928)
munro_repository.save(munro253)

munro254 = Munro('Meall nan Eun', 928)
munro_repository.save(munro254)

munro255 = Munro('Moruisg', 928)
munro_repository.save(munro255)

munro256 = Munro('Ben Hope', 927)
munro_repository.save(munro256)

munro257 = Munro('Eididh nan Clach Geala', 927)
munro_repository.save(munro257)

munro258 = Munro('Beinn Liath Mhor', 926)
munro_repository.save(munro258)

munro259 = Munro('Beinn Narnain', 926)
munro_repository.save(munro259)

munro260 = Munro('Geal Charn - Monadhliath', 926)
munro_repository.save(munro260)

munro261 = Munro('Meall a-Choire Leith', 926)
munro_repository.save(munro261)

munro262 = Munro('Seana Bhraigh', 926)
munro_repository.save(munro262)

munro263 = Munro('Stob Coire Raineach - Buachaille Etive Beag', 925)
munro_repository.save(munro263)

munro264 = Munro('Creag Pitridh', 924)
munro_repository.save(munro264)

munro265 = Munro('Sgurr nan Eag', 924)
munro_repository.save(munro265)

munro266 = Munro('An Coileachan', 923)
munro_repository.save(munro266)

munro267 = Munro('Sgurr nan Each', 923)
munro_repository.save(munro267)

munro268 = Munro('Tom na Gruagaich - Beinn Alligin', 922)
munro_repository.save(munro268)

munro269 = Munro('An Socach - Affric', 921)
munro_repository.save(munro269)

munro270 = Munro('Sgiath Chuil', 921)
munro_repository.save(munro270)

munro271 = Munro('Carn Sgulain', 920)
munro_repository.save(munro271)

munro272 = Munro('Gairich', 919)
munro_repository.save(munro272)

munro273 = Munro('A-Ghlas-bheinn', 918)
munro_repository.save(munro173)

munro274 = Munro('Creag nan Damh', 918)
munro_repository.save(munro274)

munro275 = Munro('Meall na Teanga', 918)
munro_repository.save(munro275)

munro276 = Munro('Ruadh Stac Mor', 918)
munro_repository.save(munro276)

munro277 = Munro('Sgurr a-Mhadaidh', 918)
munro_repository.save(munro277)

munro278 = Munro('Carn Aosda', 917)
munro_repository.save(munro278)

munro279 = Munro('Geal-charn - Drumochter', 917)
munro_repository.save(munro179)

munro280 = Munro('Beinn a-Chleibh', 916)
munro_repository.save(munro280)

munro281 = Munro('Beinn Teallach', 915)
munro_repository.save(munro281)

munro282 = Munro('Ben Vane', 915)
munro_repository.save(munro282)


bag1 = Bag(climber1, munro1, 'great climb, enjoyed it')
bag_repository.save(bag1)

bag2 = Bag(climber3, munro1, 'knackered, too old for this shit!')
bag_repository.save(bag2)

bag3 = Bag(climber1, munro2, 'had a super time')
bag_repository.save(bag3)

bag4 = Bag(climber2, munro2, 'too crowded!')
bag_repository.save(bag4)

print(climber_repository.munros(climber1))
print(munro_repository.climbers(munro1))
pdb.set_trace()