import numpy as np
import math

# this is a placeholder example frame, directly outputted from getFrame
frame = [25.987211218921345, 26.610745621759634, 26.716612892933256, 26.279110654733415, 26.256183548953857, 25.853562224848304, 26.119669167033578, 26.417230206031547, 26.19172739064146, 25.92137821893249, 26.29493186530641, 25.908057361063925, 26.20933930142894, 26.03783684617497, 26.582155077427444, 26.166221462183273, 25.788083687427388, 26.05730189779365, 26.239668736011083, 26.4314767452027, 26.113707886698705, 25.846174753671107, 25.655588810882193, 25.864982643411054, 25.8378630453592, 25.638794667050718, 25.86140879348386, 26.094063805074086, 25.741162971496408, 25.850051543682355, 26.6524474538258, 26.961332363967244, 25.99499766834481, 26.60764113979502, 26.510102720734608, 26.433376899813652, 26.591319640906136, 26.013493976368295, 26.16561572636607, 26.1296796076154, 26.094074718739535, 26.060400201275797, 26.32989951344547, 26.297829636763254, 26.1308811168297, 26.066674056468173, 26.187798667485197, 26.193587128217985, 26.20006362298335, 26.231031839549246, 26.2737714762456, 26.211260347067764, 26.271000686035848, 26.401538590143332, 25.836825715011173, 26.040243910879155, 25.741575134767004, 26.27078623936177, 26.033469860701985, 25.93059415755897, 25.5305411527425, 26.03024132447075, 26.323730676114337, 26.724920632873477, 26.64572204130826, 26.670421484375368, 26.584546393050005, 26.45592250613953, 26.02815851659261, 26.079900894807054, 26.439505019045953, 26.40538985332887, 26.24945615998712, 26.12669935370559, 25.938569074092413, 26.152838322558523, 25.98446151236874, 25.931193189923306, 26.002270221160643, 26.175865043508452, 26.45612502073857, 26.074836896877173, 26.373796022226713, 26.38898960337343, 26.152662030953252, 25.893295532193747, 26.29505673081917, 25.765345799085026, 25.984866397871997, 26.07256262139765, 25.735287985220282, 25.769760262821137, 26.00939731770086, 25.98872205507905, 26.40812237333779, 25.806107257267797, 26.217012925719303, 26.412828982991073, 26.22909449367927, 26.393885302596004, 26.491767304197253, 25.916441720064654, 26.160276323557696, 26.121098928540334, 26.155809861422313, 26.2456868131452, 26.321559146600634, 26.179309284615044, 26.140982957725612, 26.05893049268866, 26.261289347540753, 25.96952843224176, 26.166444740643044, 26.12266969574074, 26.068339238391445, 26.404571099750967, 25.95458111325587, 26.249645172267094, 25.939232638466876, 25.774646344598864, 26.266123319317558, 25.92485619244337, 25.735332104225392, 26.06268015779824, 26.019040076039175, 25.778670267400344, 25.997118487376383, 26.03500626941718, 26.69642084917149, 26.413143550462053, 26.41001205228048, 26.362175045233982, 26.147611974318806, 26.208418965305498, 26.27722926903965, 26.490875850908537, 26.205112746128464, 26.18398614130382, 26.193834677603945, 25.91220791382551, 26.259730002241497, 25.97595464076454, 26.296686939217295, 25.984707512244597, 26.22128114666259, 26.140556915767604, 26.078197271772297, 26.08730932291337, 26.304281896030147, 26.241721396006994, 26.225316142618, 26.01123206179426, 25.838044631751814, 25.73225866235441, 25.850130025034105, 25.73587358633381, 25.779856342416906, 25.875462399961464, 25.901942920794113, 25.875932058798412, 26.481172287742936, 26.669703751970815, 26.371092074581668, 26.159167190838332, 26.387038428748383, 26.18349255803156, 26.153064416081918, 26.236767093035212, 26.238999081006682, 26.16559776884361, 26.32262674485895, 26.21140901983, 26.296528022778432, 26.076116072460934, 26.18784453901668, 26.18783940171926, 26.13257712498398, 26.21692531431978, 26.270379085378522, 26.077697443242414, 26.31128543916077, 26.109491062161794, 26.007009431257472, 25.885032720295612, 25.86675120256018, 25.978783278975186, 25.817685357678158, 25.47027205205137, 25.63593122818685, 25.831547702894568, 26.002298616983296, 25.82287965434682, 26.322239238856866, 26.35785563896974, 26.449378211551732, 26.14111895739825, 26.253724053268797, 25.922826124462233, 26.19314999196223, 26.34700936330546, 25.94724140044559, 26.094544463071088, 26.054649772298376, 26.310861163291122, 26.065645224648904, 26.222886412930507, 26.481278245886188, 26.20727595977712, 26.261300129350616, 26.430041208497357, 27.30805124564381, 26.943159009176668, 26.43127609196972, 26.245901470304375, 26.266060515470656, 26.099131687355793, 25.591271950291457, 25.563448858476534, 26.039411477567057, 26.01954845564353, 26.331509581728426, 26.001319419827382, 26.329206730584644, 26.444753151914597, 26.563707807758135, 26.44901113185739, 26.414552042569028, 26.10289122666859, 26.10779229479533, 26.229982464111686, 26.059054054059004, 26.09397996863146, 26.26319691796118, 25.977190456458118, 26.419972785015602, 26.37538506350461, 26.443201270209613, 26.097032334858056, 26.291129242350564, 26.273641858487395, 26.528784930219842, 27.12444176126121, 28.5815379063734, 28.85637692854317, 26.624059481928498, 26.53154793215333, 26.24130418147263, 26.174263083808228, 26.04009735991957, 26.010119649855653, 26.115633573742855, 25.84522940451137, 26.266237463799655, 26.07944524876092, 26.434677278445577, 26.386737682307682, 26.340177741668924, 26.5113285955797, 26.324781175268583, 26.236322383866536, 26.255325313934975, 26.214693908076356, 26.390009371833116, 26.26985181535889, 26.08357470745318, 26.05141536071318, 26.30993727242793, 26.29978398215917, 26.418560296371083, 25.85902171884692, 26.02246937162971, 26.16640517388862, 27.09573455311198, 30.28903495873027, 35.76733055807114, 33.48635258778501, 27.81625707047533, 26.78589323847507, 26.016137032683275, 26.32393467574633, 25.95773415230792, 25.86441599714965, 25.968174523241487, 26.09390171406727, 26.09930910444018, 26.07855571448283, 25.97567434617605, 26.30137655441689, 26.1379218556375, 26.284237526420327, 26.13393081450016, 26.291496599375023, 26.22852335302497, 26.15740801782306, 26.019309868463665, 26.235799667149024, 25.96337222792772, 25.883914787590186, 26.208004110603838, 26.345882614191964, 26.307529939147344, 26.078447140640947, 26.336608236397467, 26.124118599004646, 27.414026070417947, 30.96950308980604, 36.05673196484412, 33.707977654680576, 27.493062433304203, 26.28942775500292, 26.075834910458468, 26.270084585106076, 25.929666606562876, 25.925155396338937, 26.16307927420206, 25.87689690401345, 25.925736885318884, 26.109493384872167, 26.068290630117588, 26.408614389723937, 26.34726485196086, 25.922049382213856, 26.422319762694485, 26.020797733291317, 26.219017206797048, 25.981042695373617, 25.95146963243758, 25.632851269457035, 25.966070549991514, 26.017477134943476, 26.287019246552745, 26.293179733638112, 26.249904693882854, 26.141482885327036, 26.09356214159095, 25.81845210095878, 26.491922833708543, 27.10490891227795, 29.678292281973313, 28.386368794775706, 26.275051906466558, 26.19746452075742, 26.142136078714657, 25.99063066824516, 25.981531655124684, 25.713151238787418, 26.116989832203956, 25.77367052358369, 26.09165979954713, 26.16514092366657, 25.953044055262467, 26.780423354431832, 26.9041267129399, 26.428426463649373, 26.642010083752666, 26.058918395511512, 26.177389813699676, 26.02007138239719, 26.003606499709917, 25.991469601829465, 26.02166812823998, 26.044488552569135, 26.151291982654584, 26.1470461333746, 26.313708731878705, 26.08166961613398, 26.12965360918662, 26.19572761786185, 26.032439350614197, 26.18389823898326, 26.7059009903586, 26.63402566891324, 26.23703496753666, 26.126001924738887, 26.001289643392226, 26.091556968639907, 25.939617957166718, 26.193635709717, 26.186133658341134, 26.065451972361927, 26.158412796483333, 26.029151003359743, 26.519660647634396, 26.18982914719328, 26.49091332634947, 26.382277630212855, 26.186057863928795, 26.3913425868447, 26.027091614231495, 25.50827661907391, 26.002265965347647, 26.01956468593795, 25.841627987389643, 25.90336638284765, 26.14146136655438, 26.11491502741876, 26.30162007009426, 26.091986400405915, 26.231930902362535, 26.148645890729142, 26.087462006951853, 25.926538865636473, 26.152603908208675, 26.229107001967805, 26.043611207327046, 25.972752135397116, 26.167583472526417, 25.900993689139284, 25.89185731905559, 26.014336331100765, 25.936156337913815, 26.095116835429167, 25.929803599377863, 25.74803046222428, 26.74102790331375, 26.61821077124489, 26.72368034691931, 26.26234149309994, 26.520580339592584, 25.908574430841384, 25.84657484351385, 25.866106584590852, 26.013410034348, 25.83506212582523, 26.0579256995224, 26.201000052183986, 26.17819619418242, 26.226221728572796, 26.083563566821226, 26.013190914370057, 26.079966934763092, 26.322432798362627, 26.449407281983838, 26.604024749635016, 26.769638401204645, 26.243648231320833, 26.17168143746943, 26.05525811988838, 26.010932047788003, 26.13141089773586, 25.93338730184172, 26.02073079270042, 26.198382523309988, 26.217490552019967, 26.118525630865406, 25.894671080962098, 26.469106367710594, 26.484219127145934, 26.792869002987914, 26.198153079773363, 26.20874483759269, 26.16282587531839, 25.931851801281482, 25.953420466299576, 25.848215554073704, 26.057262691424, 26.091250667572695, 26.25493921186512, 26.07586667508741, 26.138582094719254, 26.195043013613713, 26.114367025135095, 26.240234359890962, 26.224513632682886, 29.170615917827604, 31.53879371094098, 32.15898328245214, 30.129005537479088, 26.354854318172272, 26.22457263137585, 26.15289769126275, 25.877595474143277, 26.209107548716133, 25.807143591754084, 26.297939848052863, 25.979290919297284, 26.402349517318896, 26.027789034900593, 26.84303021822126, 26.643306218637292, 26.98612211379708, 26.215545947939574, 26.382405055656193, 26.032526554657636, 26.191515854099805, 26.172958226846674, 26.19278498193887, 26.244255648579895, 25.915388811290427, 25.847462698202605, 26.192467395405913, 26.124014507886898, 26.29046516860808, 26.28551897508936, 26.511858262345243, 26.559851861901905, 29.71624066080591, 33.28727196126084, 33.81821183221223, 30.672971816456936, 26.822016139436982, 26.400968641598638, 26.359802016427125, 26.167369870198513, 26.01741107769317, 25.6760518469535, 25.934613968711233, 26.252907300042466, 26.29867560178525, 26.011343297659096, 26.88408701323226, 27.015519297016965, 28.444403906120897, 27.73548248856565, 26.380205389394803, 26.341617019787236, 26.158313943861344, 25.88290420915638, 25.9469280258881, 25.99399622144921, 26.213141253661206, 25.844611225621293, 26.044903315622662, 26.35865959528212, 26.397066954548336, 26.280484378898677, 26.531057235506125, 26.66917562075372, 28.152803037493015, 29.243657351428396, 30.11103648781767, 28.38021612677511, 26.59104279998178, 26.314762481966852, 26.26991562534738, 26.216988518597304, 26.089181186989947, 26.019890961921476, 26.28580240006511, 26.21795789096592, 26.662189926124483, 26.33125964153163, 26.693098580578862, 26.705437792595774, 29.784820849462562, 28.67715951156231, 26.966352815113453, 26.343244802175832, 26.2853173951969, 25.991864967563572, 26.169350735492287, 26.19732222799928, 26.10520649181109, 25.922453758733752, 26.126261687805368, 26.1207139066197, 26.193000511076605, 26.510608424619306, 26.508349499557937, 26.375864637449467, 26.894956890730725, 27.70264604866179, 27.673046911401002, 27.152784791222643, 26.48917840198493, 26.39056735806355, 26.255622560733286, 26.268673367768656, 26.651885598130036, 26.443577726238345, 26.158036571144862, 26.199844417207657, 26.385146908506044, 26.44821625067118, 26.878033473747166, 27.04356217603356, 30.53354060905633, 30.192703690605867, 28.577892304447175, 27.314949344292927, 26.4336983593102, 26.11567352391711, 26.2417037791119, 26.022321107759865, 25.97449054464863, 25.786030843634023, 26.2316928851792, 26.202851068984955, 26.537535814779062, 26.184421474206204, 26.551327663588154, 26.52493554476638, 26.574871034659566, 26.404941739045967, 26.733745473875558, 26.484743438666044, 26.680347952002023, 26.579994716416195, 27.7097302575865, 28.036758254061056, 27.117063605191447, 26.639497072394363, 26.430241266423195, 26.54492366959761, 26.731154857324384, 26.419929839452948, 27.18252050408836, 27.174638656278432, 30.785946834868525, 30.58775564679007, 29.09271032289297, 28.351810570583098, 26.033458332526152, 26.080583443330568, 26.46725762615813, 26.44050241455517, 26.291912991405695, 26.035175713213732, 26.61491287349338, 26.258427615000073, 26.40666097891983, 26.214959570324083, 26.63338653413001, 26.567129028332147, 26.52896386668175, 26.454161904585646, 26.602432615678822, 26.529287527230565, 26.646580374413077, 26.299200201548672, 27.920764988235874, 28.79637225632166, 27.59846945485276, 26.952193188780313, 26.70425917183468, 26.795891681699118, 26.72517108735684, 26.703080312494137, 27.03251531526007, 27.323932277095196, 31.11844535649584, 30.909449220681097, 30.35886294219563, 29.90434447604366, 27.06181932764872, 26.64126833198344, 26.403712240360733, 26.529212814873915, 26.18173550241744, 26.408780337037285, 26.42657958659845, 26.377331931844253, 26.355577012898266, 26.442932170627046, 26.691329862958412, 26.49081203486037, 26.506154934461335, 26.29628988842404, 26.702405764132493, 26.724696041800144, 26.171334223028452, 26.13617228781493, 27.22611732921746, 27.43436424412056, 26.810344896127503, 26.273894391306328, 26.967731152760848, 26.658144160533823, 26.689818782930615, 26.88012150627992, 27.0436642484608, 27.486015571947064, 31.064179031438016, 30.815092569681156, 30.46403303045372, 30.452918362870946, 27.816023886209962, 27.049599675639115, 26.799150226740835, 26.38283979107149, 26.162895922707435, 26.33914033922133, 26.383486655949753, 26.431861780666736, 26.628382245720616, 26.2664307068963, 26.315275241964628, 26.415985608549192, 26.58619820593526, 26.225589552176075, 26.523879235926188, 26.503087569116417, 26.166775361825785, 26.55248467064513, 26.45302492918887, 27.156905770953813, 26.41614955949302, 26.619607088009218, 26.950761021679227, 26.916021691998424, 26.68534693745545, 26.855324643715164, 26.744400892204624, 27.44946170277865, 30.885607775854112, 31.01964301640936, 31.24278707656481, 31.076719787863, 30.055923494053104, 28.85193224546549, 27.340229394700998, 26.828087195923274, 26.551164945307733, 26.512343999885843, 26.355807425338412, 26.65670994835665, 26.365436086272325, 26.020931718437282, 26.522206682526075, 26.035196758690347, 26.404493967847543, 26.308326058971545, 26.532879291381334, 26.305495904299903, 26.535582589646594, 26.232814863126976, 26.72906697143293, 26.708138989703457, 26.75059829807344, 26.58164024200852, 27.024376586878077, 27.14239941035879, 26.961181207826712, 26.869054197457956, 27.994543480691675, 28.653965155124865, 30.702988723215412, 31.462739017658805, 30.888218830032486, 30.861177461257228, 30.49677236668697, 29.85780388612136, 27.99177116711047, 27.25571332976955, 26.125420233083616, 26.342410653795753, 26.18642080705365, 26.38320622277263, 26.208457393234653, 26.464830381738523, 26.491839095631462, 26.364662912629, 26.627822138837473, 26.511834095013057, 26.399947303519355, 26.37157313299349, 26.414493926015382, 26.57480229662167, 26.46535777996229, 26.827777944913976, 26.349458402822734, 27.01968541293496, 26.899069886292466, 26.945594166629405, 26.80911281413006, 27.124918801424997, 27.84065590624533, 28.18677323555255]
frame = np.array(frame)
frame.shape = (24, 32)

# i'll add more thresholds later to meet requirements
thresh1 = 35
# set of tuples that have already been 'claimed' by a cluster of pixels above threshold
already_clustered = set()
# list of tuples of form (size, temperature)
clusters = []

# this finds the size of the cluster of pixels above the threshold temperature
def findNeighbors(i, j, thresh):
    if (i < 0 or j < 0 or i >= len(frame[0]) or j >= len(frame) or (i, j) in already_clustered):
        return 0
    if (frame[i][j] >= thresh):
        already_clustered.add((i, j))
        return 1 + findNeighbors(i+1, j, thresh) + findNeighbors(i-1, j, thresh) + findNeighbors(i, j+1, thresh) + findNeighbors(i, j-1, thresh)
    return 1

# now we loop through the pixels, and if a pixel is above the threshold and not already part of a cluster,
# then we find its cluster size
for i in range(len(frame)):
    for j in range(len(frame[0])):
        if ((i, j) not in already_clustered and frame[i][j] >= thresh1):
            neighbors = findNeighbors(i, j, thresh1)
            clusters.append((neighbors, thresh1))


for x in clusters:
    print(x)
