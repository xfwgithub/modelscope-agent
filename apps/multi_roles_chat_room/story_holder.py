import os

STORY_1 = """用户是男主角顾易，与多位长相、性格都大相径庭的美女相识，这几位美女都喜欢顾易，相互之间争风吃醋，展开一段轻喜甜蜜的恋爱之旅，除了顾易之外，其他几个角色之间一定要互相冲突打击对方。
"""

ROLES_1 = {
    '顾易': '男主角，与多位美女相识，被美女包围，展开一段轻喜甜蜜的恋爱之旅',
    '郑梓妍': '郑梓妍，23岁，射手座，A型血，鬼点子大王，极致魅惑，职业：杂志编辑',
    '李云思': '李云思，27岁，摩羯座，O型血，趣味相投的知音，温婉大气，职业：策展人',
}

STORY_2 = """用户是男主角雷军，小米创始人，最近发布了小米SU7，与多位新能源的创始人都认识，大家都在竞争卖车，雷军公布价格后，他们都很慌，害怕自己的车卖不出去。"""

ROLES_2 = {
    '雷军': '小米创始人，最近发布了小米SU7，投资界之王，有很强的人缘，投资了很多公司。小米SU7的口号是【人车合一，我心澎湃】',
    '李想': '理想汽车，是由李想在2015年7月创立的新能源汽车公司，公司最初命名为“车和家，卖的最好的是理想L系列”',
    '李斌': '蔚来汽车创始人、董事长，也是新能源的早期创始人之一，之前做易车网',
    '何小鹏':
    '何小鹏同时担任小鹏汽车的董事长。小鹏汽车成立于2014年，小鹏汽车最热销的系列是小鹏P7，受影响最大，所以此次小米发布价格对其冲击很大'
}
STORY_3 = """用户是庆余年男主范闲，在第一部中被二皇子算计自杀诈死，与多位女子都有过深入接触，也被多个女子所喜爱"""

ROLES_3 = {
    '范闲': ('由张若昀饰演。尚书范建的养子，叶轻眉与庆帝的儿子。外形俊美，喜怒不形于色，深藏绝世神功。'
           '在功成名就之后归隐江南。结识了不少美丽动人的女子，与她们有过爱恨情仇。'
           '包括林婉儿，海棠朵朵，战豆豆和司理理'),
    '林婉儿':
    ('林婉儿是电视剧《庆余年》中的女主角，由演员李沁饰演，剧中为庆国宰相林若甫与长公主李云睿之女，范闲的正夫人。'
     '她性格活泼开朗，善良正直，爱打抱不平，也爱吃鸡腿，因此有“鸡腿姑娘”的外号。她对范闲一见钟情，两人经历了许多波折后终于走到一起，成为了令人羡慕的夫妻。'
     '她身体不好，患有肺结核，后来在范闲的努力下治愈了病痛，并为范闲生下了一个儿子。最后她与范闲隐居田园，过着幸福的生活。'),
    '海棠朵朵':
    ('海棠朵朵是北齐苦荷的关门弟子，身兼圣女重任，村姑模样的打扮与做派让她成为众多九品高手中的异类。'
     '范闲出使北齐的路上遇见了海棠朵朵，两人性情相投十分的默契，后来海棠朵朵也陪伴范闲经历了很多的风雨。'
     '范闲和海棠朵朵之间有着深厚的友情和爱情，但是由于身份和国家的原因，他们始终不能公开在一起。虽然海棠朵朵和范闲之间都彼此有好感，但是两个人最终却没有在一起。',
     ),
    '战豆豆':
    ('战豆豆是北齐皇帝，一生最大的夙愿是比肩甚至超越那位庆国的伟大皇帝，但可惜的是女儿身让她处处受制。'
     '毕竟不是谁都能成为武则天的，后在四顾剑庐中与范闲同房，生下一个女儿小名取为“红豆饭”，由此可见这位女皇帝虽身居高位，但终究还是带有小女人心态的。'
     '战豆豆对范闲有着复杂的情感，既有敌意又有爱意，她曾经想过用各种手段留住范闲，但是最终还是放弃了。她最后的结局也是终身隐瞒自己女儿身的事实，终身守护北齐国。'
     ),
    '司理理': ('司理理是北齐国派来的密探，真实身份是庆国皇室血脉，由于夺权事件被迫远走异国他乡。'
            '她与范闲相识相知，对他产生了不一样的感情。她曾经为了保护范闲而受尽酷刑，也曾经为了帮助范闲而背叛了自己的国家。'
            '她对范闲的爱情是无私而忠贞的，但是却没有得到回报。她最后为了维护北齐国的尊严，选择留在北齐皇帝战豆豆身边充当爱妃。'),
}

stories = [
    {
        'id': '1',
        'cover':
        '//img.alicdn.com/imgextra/i4/O1CN019AOpae1C8XD0EQYzL_!!6000000000036-0-tps-597-333.jpg',
        'title': '我被美女包围了',
        'description': '用户是男主角顾易，与多位长相、性格都大相径庭的美女相识',
        'roles': ROLES_1,
        'story': STORY_1,
        'default_topic': '@顾易 要不要来我家吃饭？'
    },
    {
        'id': '2',
        'cover':
        '//img.alicdn.com/imgextra/i3/O1CN01JuIxJr1V5J7OF7fLP_!!6000000002601-0-tps-597-333.jpg',
        'title': '我是雷军，雷中有“电”，军下有“车”',
        'description': '用户是男主角雷军，小米创始人，最近发布了小米SU7',
        'roles': ROLES_2,
        'story': STORY_2,
        'default_topic': '@雷军 雷总啊，你这定价太狠了，发布直接21.49万，兄弟们都不好卖车了啊'
    },
    {
        'id': '3',
        'cover':
        '//img.alicdn.com/imgextra/i3/O1CN01bDTQi01kIn1ABfMHE_!!6000000004661-0-tps-640-360.jpg',
        'title': '庆余年，范闲身边的女子',
        'description': '用户是庆余年男主范闲',
        'roles': ROLES_3,
        'story': STORY_3,
        'default_topic': '@范闲 范闲，听说你被二皇子杀了，快回话啊'
    },
]


def get_story_by_id(story_id):
    for story in stories:
        if story['id'] == story_id:
            return story
    return None


def get_avatar_by_name(role_name):
    # get current file path
    current_file_path = os.path.abspath(__file__)

    # get current parent directory
    parent_directory_path = os.path.dirname(current_file_path)
    file_map = {
        '顾易': 'guyi.png',
        '郑梓妍': 'zhengziyan.png',
        '李云思': 'liyunsi.png',
        '林婉儿': 'linwaner.jpeg',
        '范闲': 'fanxian.jpg',
        '战豆豆': 'zhandoudou.jpg',
        '海棠朵朵': 'haitangduoduo.jpg',
        '司理理': 'silili.jpeg',
        'others': 'default_girl.png'
    }
    if role_name not in file_map.keys():
        file_name = file_map['others']
    else:
        file_name = file_map[role_name]
    avatar_abs_path = os.path.join(parent_directory_path, 'resources',
                                   file_name)
    return avatar_abs_path
