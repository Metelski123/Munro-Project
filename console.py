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

munro156 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro157 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro158 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro159 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro160 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro161 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro162 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro163 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro164 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro165 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro166 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro167 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro168 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro169 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro170 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro171 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro172 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro173 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro174 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro175 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro176 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro177 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro178 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro179 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro180 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro181 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro182 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro183 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro184 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro185 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro186 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro187 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro188 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro189 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro190 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro191 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro192 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro193 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro194 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro195 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro196 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro197 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro198 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro199 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro200 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro201 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro202 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro203 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro204 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro205 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro206 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro207 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro208 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro209 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro210 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro211 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro212 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro213 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro214 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro215 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro216 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro217 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro218 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro219 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro220 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro221 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro222 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro223 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro224 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro225 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro226 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro227 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro228 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro229 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro230 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro231 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro232 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro233 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro234 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro235 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro236 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro237 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro238 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro239 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro240 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro241 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro242 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro243 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro244 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro245 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro246 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro247 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro248 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro249 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro250 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro251 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro252 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro253 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro254 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro255 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro256 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro257 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro258 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro259 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro260 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro261 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro262 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro263 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro264 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro265 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro266 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro267 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro268 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro269 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro270 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro271 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro272 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro273 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro274 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro275 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro276 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro277 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro278 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro279 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro280 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)

munro281 = Munro('Ben Macdui', 1309)
munro_repository.save(munro2)

munro282 = Munro('Ben Nevis', 1345)
munro_repository.save(munro1)


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