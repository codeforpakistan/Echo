import csv
import re
import csv

def write_parameters(read,write)
	filee =open(read) #omer.txt
	fie=filee.read()
	fie =re.sub('{', '', fie)

	J=fie.split(",")

	    
	    
	count=1;
	L=[]
	for i in J:
	    if(i[-1]!="}"):
		L.append(float(i))
	    else:
		i=re.sub("}","",i)
		L.append(float(i))
		

		with open(write, 'a') as myfile:
		    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		    wr.writerow(L)
		
		
		L=[]
		print "added" ,count ,"row"
		
		count+=1
	with open("Array_C.csv", 'a') as myfile:
		    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		    wr.writerow(L)
		
	print "Done"    



	"""
	L1=[-616.95916088582908, 32.226962227656465, 1.5078346350297298, -5.752516766568883, -6.594230536205373, -0.42076590691079263, 0.26427795615118993, 7.3832645586951022, 7.7934540556910807, 6.8212659028125158, 5.3832428007023925, 7.9525211835211023, 8.6477587341631619, 6.7261702304782585, 6.0998243826056164, 6.7619339172794426, 6.4194579589482048, 5.6691213633573119, 4.8708793445069389, 6.005427877817902, 4.7924657650078473, 5.6879689138022007, 5.3240637582973802, 5.0486614299450174, 5.1339727228369885, 5.768339716750809, 4.5471705224841417, 5.0224749441380805, 4.681421429099478, 4.928582645421959, 4.025646403554191, 4.5458991631103203, 4.5398736807613513, 4.4449773858657959, 4.4255544548018424, 5.2847879317560702, 4.5278048703979028, 4.6371995689770458, 3.8380547956730999, 4.4396668419527714, 4.2444058421686055, 4.743506711151662, 4.1722890665003574, 4.6952478982378647, 4.4145207887724576, 4.239669162181686, 4.3448541423454525, 4.1589041409406171, 4.2224483599828346, 4.2741137608292075, 3.9122883969155424, 4.090614295479658, 3.70650818768407, 3.7621978153874176, 3.3290929792933119, 3.9525019382272975, 3.8229913794926382, 3.3703450643419006, 2.8566904504820281, 3.3073202809519753]

	L2=[-0.5973632147900878, -0.37041227344787453, -0.51401500239689479, -0.26676489784695162, -0.63949841553853248, -0.66550312487282093, -0.72116061177710544, -0.22321150768196713, -0.60888608470463312, -0.4459577919025921, -0.084122003312380011, -0.18789492443243158, -0.89013647678280006, -0.20962949169488229, -0.40761749512803463, -0.36828156697787001, -0.77050111222609974, -0.35919507681524787, -0.39358939961383616, -0.50952002341234637, -0.78951851809525364, -0.71924780890610962, -0.015042124923725718, -0.46124745061553774, -0.38857734556887924, -0.36079759593172167, -0.14705003947132869, -1.2204164749044817, -0.056151049911810663, -0.60500135936827659, -0.88803595198866858, -0.37349614559475208, -0.66767400542214905, -1.9350492452537797, -0.10772525249594234, -0.40318127106403395, -0.17842743226018995, -1.0044694012962636, -0.35627396590293603, -0.27675081329489393, -0.27532701701730378, -0.66231597036629741, -0.66101884856013948, -0.36162795387494284, -0.10985903337334517, -0.29069793502383151, -0.42291214221570173, -0.52123606626458596, -0.12774943043698614, -0.33370392852113417, -0.35846764509818718, -0.76956816196536404, -0.71680815103307405, -0.4772072575042034, -0.18310053445059465, -0.32776233107263819, -0.41983133664496408, -0.15956859807248938, -0.30464646583260069, -0.54336438491735672, -0.22424720101017095, -0.060882069128953123, -1.609905311643391, -0.063035370951967873, -0.31077165353363756, -0.42251587087567488, -0.66328941804356034, -0.27200272446700346, -0.49783286431793344, -0.13684339622253486, -0.78916135764756734, -0.64718917113037899, -0.49821569962863355, -0.78413775765558369, -0.29775424764336628, -0.51393021467654898, -0.14159184029793828, -0.42738154572676323, -0.38719404366729643, -0.42770616544203233, -0.19968569857110324, -0.26756467709684767, -0.67781380448308259, -0.34091433438929863, -0.15589570819290396, -0.53359979743463404, -0.96260508136011269, -0.81183021162704816, -0.67050988423632629, -0.40886919543643541, -0.66185201277580252, -0.21260941595289873, -0.66100206838771203, -0.21614078328579447, -0.58796595313104572, -0.16337306716188729, -0.71621822860686857, -0.34872900433214221, -0.5148617129565507, -0.43104238377164455, -1.1611150012562661, -0.39868675600740799, -0.19461583129364926, -0.10534414192833533, -0.54167213401983927, -0.75938825820417044, -0.90278503443526337, -0.40894726745780818, -0.70289392787929528, -0.53197378209401813, -0.46078148026428367, -1.3183687478621067, -0.8385137337721853, -0.34781041123269807, -1.2905637760601458, -0.63707371128793722, -1.6659959409659029, -0.63372477964393514, -0.31050357544802176, -0.39605282111630752, -0.74702367116464174, -1.9429057007510415, -0.93781675177715584, -0.2949494253236894, -0.10283701963000483, -0.71814650126548951, -0.20295534942058949, -0.78592568740941571, -0.35227705217471267, -0.46772702350481782, -0.66591652026179271, -0.95486674180011133, -0.22245386104348955, -0.40958388241387145, -0.12387673210012584, -1.7678713370848693, -0.15720689000138033, -0.15882973156712069, -0.58501856003327757, -0.47304674575269023, -1.0568559364752508, -0.25412365292773653, -0.66351174656788703, -0.58422920095784237, -0.67962354364193578, -0.026592871666096397, -0.26404794796685982, -0.59396570547470873, -1.6791799085887176, -0.67360401871512954, -0.26850537685733056, -0.33636783040190865, -0.67959908793949853, -0.61645141693633954, -0.62173837886721972, -0.29360340943988422, -0.74961474407141582, -0.086138032816924059, -0.024356993626134135, -0.79683031418432926, -0.55794189909308056, -0.55964332959195628, -0.27061810887172416, -0.53176869337659716, -0.75428616280179384, -1.004151065607308, -0.23103563161106974, -1.5483812528416339, -0.44534939356409126, -0.69203451731640975, -0.4830644367119854, -0.30437999793470566, -0.88498304712175146, -0.39305354569790074, -0.20556507724330697, -0.51962159535223473, -0.81770921018027287, -1.7508024964162627, -1.2796469231927574, -0.52027040740362274, -0.29169495057935879, -0.50199341400716246, -0.62317497105948172, -0.68858726328315822, -1.6456055613117937, -0.028581774105554712, -0.43325563466193068, -0.31271731987445894, -0.38305948909862186, -0.60584518559010747, -0.67907824740558753, -0.14770067465259454, -0.68919675776985667, -0.34912430638575787, -0.96724131353924681, -0.46511693833724277, -0.19846667765014966, -0.020479385236101287, -0.0031507555777630309, -0.71844089117879362, -0.38593585835680216, -1.1692716265970591, -0.65050493818723054, -0.58146087366915211, -0.57465207641321037, -0.82106354482778976, -0.63288916989454702, -0.71082151547361849, -0.43395391228628921, -0.31371069522910777, -0.18651132192749648, -0.038021566202243236, -0.90243577431460664, -0.49150100456421097, -0.66829626061560077, -0.28951656367529227, -0.66520536086917992, -0.037536849154864139, -0.8179254923930428, -0.50858555291141749, -0.57045653336643265, -0.47920410975226174, -1.1300830748279156, -0.4206973497095664, -0.0023438408560849883, -0.68156798417373676, -0.63290430761349936, -1.1989190444566262, -0.70290364782918624, -0.44462081992591795, -1.7162517428305941, -0.53106394597381379, -1.1376778000881549, -0.64674601982687896, -0.098624052282684116, -0.27149885181803679, -0.37441358390796331, -0.50836996724394445, -0.66338303454685299, -2.0833341753922356, -1.0828095286847441, -0.90721171222229724, -0.93834340580984277, -0.52574796383029343, -0.042538590397836182, -0.36108780588313538, -0.94934654345217184, -0.43007182595949656, 0.87354048952225738, 0.24135186542255044, 1.2547894516309797, 1.0268429088247473, 0.14475397256042974, 1.2744048559322905, 1.465065446337892, 1.4451770261842618, 1.4506178020870668, 0.89869078613432285, 0.1895320794667017, 0.56088675777625663, 0.53306180625469479, 0.25997040711604097, 0.7754460391486494, 1.0719080529168847, 0.75707979147144, 0.071598278622727829, 1.1608453820134372, 0.39596417541580503, 1.0728128004730031, 1.024650729089104, 1.1133087075455808, 1.0139909115013237, 0.1792740100815822, 1.3819421199084816, 0.11229593889775484, 1.0416073625636133, 0.4521463730601602, 0.6661885759858831, 0.52217380773062239, 0.70162830380736052, 0.85150454325882408, 0.16032827355763288, 0.25646596499356028, 1.0762946656875119, 0.010949805838162669, 1.776670168836606, 0.31279917143816094, 1.1719687182899374, 0.114089520201498, 0.19421331032678399, 0.69524421956005156, 0.20738546895736182, 1.0503329167413795, 0.13008776538113312, 0.80471633315594659, 1.1147891832858712, 0.24399763573460523, 0.61917866150159417, 0.69352710417695507, 0.8345274765774634, 0.78444068028622316, 0.057760631209688926, 0.55887961869202929, 0.8781378307917943, 0.64399532557669725, 0.59061714586123626, 0.74012471071744113, 1.2624920213656843, 1.40865056543568, 1.2133623337476345, 1.3059667583753998, 0.64208838185917405, 0.30007650508430489, 0.34566780928157692, 0.34818233364312801, 0.73869223382050575, 1.1717009475275419, 0.82182522910275613, 0.45009342912557271, 0.44253215927130102, 0.6806722805728197, 0.87983956604179703, 1.4586872774645052, 0.70047088632567056, 0.62338507182162073, 0.26167601148053371, 0.6910532950212378, 1.1209376630601999, 0.21679687575217602, 0.97211407000669403, 0.84279436872062696, 0.46613309252561319, 0.24515607777298623, 0.2054351689086594, 0.83612991490001287, 0.28869905199527629, 0.11182889497106799, 1.7922670902229449, 1.2474727197572519, 0.75764037938204021, 0.76210940256619486, 1.0432737783783308, 1.3801956712325005, 1.3297225016742784, 0.89419277313359702, 1.3822087629856237, 1.218601565340302, 0.41629340602455545, 1.258830525939205, 0.32986763389493551, 0.98617440083676688, 0.30941824493594061, 0.44918189611480297, 1.2603051992701171, 0.64959329554064826, 0.5884288012257225, 0.66338136617883048, 0.74320625884646607, 0.68372171040809715, 0.14919338565593959, 1.3167130841354069, 0.24728411279403592, 1.0634112759087009, 1.0499408104649839, 0.21181199625498143, 1.6150416000350059, 0.52197855983053176, 0.97727084269231057, 0.87955546807538676, 1.9069438846776625, 1.6922707285467271, 1.0205832492560099, 1.1827231572488339, 1.8920513353394084, 0.84879040894015367, 1.131299541905832, 1.2490591244819456, 1.0090390523006281, 1.3362166756027132, 0.3518971406996258, 0.74249731981188127, 0.54127678036303573, 0.17394952215374421, 0.2595686055895246, 0.10565223522060163, 1.3427421603864489, 1.01022356971109, 0.25238193296647449, 1.1444434688302205, 1.0903661415501815, 1.0724280172385372, 0.41454103581701934, 0.71800004192782541, 0.84383347524767827, 1.0106670737853563, 1.5332872459259623, 0.72820409036983869, 1.0128238370775489, 1.3578178098288636, 0.47391605861334712, 0.70185326994062269, 0.42009353421370932, 0.34987577922478758, 0.66814184208060223, 0.6077877755075568, 1.1901187832000342, 0.44485471938870658, 0.53344192364380505, 0.39854372101862817, 0.42498489492339148, 0.042479100316274734, 0.5889826795890396, 0.072544477938483787, 0.68106043782659931, 0.12194869518688056, 0.49282313973107827, 0.47200047824670605, 0.17492089230490901, 0.63710296622596196, 0.50267401244816012, 1.2777594489900981, 0.68197671637764623, 2.9053892253627476, 0.12727383575056789, 0.631964888208847, 0.6870492217096893, 0.17619176089840119, 1.0773282225592036]
	B=[]
	for k in L:
	    k=float (k)
	    B.append(k)
	with open("Array_B.csv", 'w') as myfile:
		    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		    wr.writerow(B)"""

