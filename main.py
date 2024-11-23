import math
from enum import Enum, unique
import json


#五行
@unique
class EElement(Enum):
    Wood = 1
    Fire = 2
    Earth = 3
    Metal = 4
    Water = 5


@unique
class EElementRelation(Enum):
    Me = 0  # 自己
    Generate = 1  # 我生
    Restrained = 2  # 我克
    GenerateBy = 3  # 生我
    RestrainedBy = 4  # 可我


#五行类
class ElementInfo:
    def __init__(self, *, name, description, element, who_i_generate, who_i_restrain, who_generate_me, who_restrain_me):
        self.name = name
        self.description = description
        self.element = element
        self.who_i_generate = who_i_generate
        self.who_i_restrain = who_i_restrain
        self.who_generate_me = who_generate_me
        self.who_restrain_me = who_restrain_me

    def __repr__(self):
        return f"ElementInfo(name='{self.name}', description='{self.description}')"

    def getRelationWithOther(self, other):
        if self.who_i_generate == other:
            return EElementRelation.Generate
        if self.who_i_restrain == other:
            return EElementRelation.Restrained
        if self.who_generate_me == other:
            return EElementRelation.GenerateBy
        if self.who_restrain_me == other:
            return EElementRelation.RestrainedBy
        return EElementRelation.Me


element_info = {
    EElement.Wood: ElementInfo(
        name="木",
        description="木性柔顺，代表生长和发展。",
        element=EElement.Wood,
        who_i_generate=EElement.Fire,
        who_i_restrain=EElement.Earth,
        who_generate_me=EElement.Water,
        who_restrain_me=EElement.Metal
    ),
    EElement.Fire: ElementInfo(
        name="火",
        description="火性炽热，代表热情和活力。",
        element=EElement.Fire,
        who_i_generate=EElement.Earth,
        who_i_restrain=EElement.Metal,
        who_generate_me=EElement.Wood,
        who_restrain_me=EElement.Water
    ),
    EElement.Earth: ElementInfo(
        name="土",
        description="土性稳重，代表稳定和安全。",
        element=EElement.Earth,
        who_i_generate=EElement.Metal,
        who_i_restrain=EElement.Water,
        who_generate_me=EElement.Fire,
        who_restrain_me=EElement.Wood
    ),
    EElement.Metal: ElementInfo(
        name="金",
        description="金性坚硬，代表坚定和果断。",
        element=EElement.Metal,
        who_i_generate=EElement.Water,
        who_i_restrain=EElement.Wood,
        who_generate_me=EElement.Earth,
        who_restrain_me=EElement.Fire
    ),
    EElement.Water: ElementInfo(
        name="水",
        description="水性流动，代表变化和灵活。",
        element=EElement.Water,
        who_i_generate=EElement.Wood,
        who_i_restrain=EElement.Fire,
        who_generate_me=EElement.Metal,
        who_restrain_me=EElement.Earth
    )
}


#天干
@unique
class ETianGan(Enum):
    Jia = 1  # 甲
    Yi = 2  # 乙
    Bing = 3  # 丙
    Ding = 4  # 丁
    Wu = 5  # 戊
    Ji = 6  # 己
    Geng = 7  # 庚
    Xin = 8  # 辛
    Ren = 9  # 壬
    Gui = 10  # 癸


#天干信息
tian_gan_info = {
    ETianGan.Jia: "甲",
    ETianGan.Yi: "乙",
    ETianGan.Bing: "丙",
    ETianGan.Ding: "丁",
    ETianGan.Wu: "戊",
    ETianGan.Ji: "己",
    ETianGan.Geng: "庚",
    ETianGan.Xin: "辛",
    ETianGan.Ren: "壬",
    ETianGan.Gui: "癸"
}


#地支
@unique
class EDizhi(Enum):
    Zi = 1  # 子
    Chou = 2  # 丑
    Yin = 3  # 寅
    Mao = 4  # 卯
    Chen = 5  # 辰
    Si = 6  # 巳
    Wu = 7  # 午
    Wei = 8  # 未
    Shen = 9  # 申
    You = 10  # 酉
    Xu = 11  # 戌
    Hai = 12  # 亥


#地支信息
dizhi_info = {
    EDizhi.Zi: "子",
    EDizhi.Chou: "丑",
    EDizhi.Yin: "寅",
    EDizhi.Mao: "卯",
    EDizhi.Chen: "辰",
    EDizhi.Si: "巳",
    EDizhi.Wu: "午",
    EDizhi.Wei: "未",
    EDizhi.Shen: "申",
    EDizhi.You: "酉",
    EDizhi.Xu: "戌",
    EDizhi.Hai: "亥"
}


#地支刑冲
class EXingChong(Enum):
    Wu = 0  # 无
    Xing = 1  # 刑
    Chong = 2  # 冲
    He = 3  # 合


#地支刑冲信息
xing_chong_info = {
    EXingChong.Wu: "无",
    EXingChong.Xing: "刑",
    EXingChong.Chong: "冲",
    EXingChong.He: "合"
}

#地支三刑
dizhi_xing = [
    (EDizhi.Yin, EDizhi.Si, EDizhi.Shen),
    (EDizhi.Chou, EDizhi.Xu, EDizhi.Wei),
    (EDizhi.Zi, EDizhi.Mao),
    # (EDizhi.Chen, EDizhi.Wu, EDizhi.You, EDizhi.Hai),
]

#地支六冲
dizhi_chong = [
    (EDizhi.Zi, EDizhi.Wu),
    (EDizhi.Chou, EDizhi.Wei),
    (EDizhi.Yin, EDizhi.Shen),
    (EDizhi.Mao, EDizhi.You),
    (EDizhi.Chen, EDizhi.Xu),
    (EDizhi.Si, EDizhi.Hai),
]

#地支六合
dizhi_he = [
    (EDizhi.Zi, EDizhi.Chou),
    (EDizhi.Wu, EDizhi.Wei),
    (EDizhi.Yin, EDizhi.Hai),
    (EDizhi.Mao, EDizhi.Xu),
    (EDizhi.Chen, EDizhi.You),
    (EDizhi.Si, EDizhi.Shen),
]


#计算空亡
def getKongWang(tian_gan, di_zhi):
    v = (di_zhi.value - tian_gan.value) % 12
    if v == 0:
        v = 12
    return EDizhi(v - 1), EDizhi(v)


#八纯卦
@unique
class EDiagrams(Enum):
    Kun = 0b000  # 坤
    Gen = 0b001  # 艮
    Kan = 0b010  # 坎
    Xun = 0b011  # 巽
    Zhen = 0b100  # 震
    Li = 0b101  # 离
    Dui = 0b110  # 兑
    Qian = 0b111  # 乾


#纯卦数据结构
class DiagramInfo:
    def __init__(self, *, name, meaning, description, element, dizhi):
        self.name = name
        self.meaning = meaning
        self.element = element
        self.description = description
        self.dizhi = dizhi

    def __repr__(self):
        return f"DiagramInfo(name='{self.name}', meaning='{self.meaning}', description='{self.description}')"

    def getRelationWithOther(self, other):
        result = []
        if self == other:
            result.append(EXingChong.Wu)
            return result

        for myDizhi in self.dizhi:
            for xing in dizhi_xing:
                if myDizhi in xing:
                    for otherDizhi in other.dizhi:
                        if otherDizhi in xing:
                            result.append(EXingChong.Xing)

            for chong in dizhi_chong:
                if myDizhi in chong:
                    for otherDizhi in other.dizhi:
                        if otherDizhi in chong:
                            result.append(EXingChong.Chong)

            for he in dizhi_he:
                if myDizhi in he:
                    for otherDizhi in other.dizhi:
                        if otherDizhi in he:
                            result.append(EXingChong.He)

        if result.count == 0:
            result.append(EXingChong.Wu)
        return result


# 使用类 DiagramInfo 存储八卦信息，每个参数一行
diagrams_info = {
    EDiagrams.Kun: DiagramInfo(
        name="坤",
        meaning="地",
        description="坤卦象征地，柔顺，厚德。",
        element=EElement.Earth,
        dizhi=[EDizhi.Wei, EDizhi.Shen]
    ),
    EDiagrams.Gen: DiagramInfo(
        name="艮",
        meaning="山",
        description="艮卦象征山，止息，稳定。",
        element=EElement.Earth,
        dizhi=[EDizhi.Chou, EDizhi.Yin]
    ),
    EDiagrams.Kan: DiagramInfo(
        name="坎",
        meaning="水",
        description="坎卦象征水，险难，智慧。",
        element=EElement.Water,
        dizhi=[EDizhi.Zi]
    ),
    EDiagrams.Xun: DiagramInfo(
        name="巽",
        meaning="风",
        description="巽卦象征风，顺从，扩散。",
        element=EElement.Wood,
        dizhi=[EDizhi.Chen, EDizhi.Si]
    ),
    EDiagrams.Zhen: DiagramInfo(
        name="震",
        meaning="雷",
        description="震卦象征雷，动荡，创新。",
        element=EElement.Wood,
        dizhi=[EDizhi.Mao]
    ),
    EDiagrams.Li: DiagramInfo(
        name="离",
        meaning="火",
        description="离卦象征火，光明，文明。",
        element=EElement.Fire,
        dizhi=[EDizhi.Wu]
    ),
    EDiagrams.Dui: DiagramInfo(
        name="兑",
        meaning="泽",
        description="兑卦象征泽，喜悦，柔和。",
        element=EElement.Metal,
        dizhi=[EDizhi.You]
    ),
    EDiagrams.Qian: DiagramInfo(
        name="乾",
        meaning="天",
        description="乾卦象征天，刚健，创造。",
        element=EElement.Metal,
        dizhi=[EDizhi.Xu, EDizhi.Hai]
    )
}


class SixtyFourDiagramInfo:
    def __init__(self, *, name, statement, meaning, description, eDiagram):
        self.element = None
        self.name = name
        self.statement = statement  # 卦辞
        self.meaning = meaning  # 含义
        self.description = description
        self.eDiagram = eDiagram

    def __repr__(self):
        return (f"SixtyFourDiagramInfo(name='{self.name}', "
                f"statement='{self.statement}', meaning='{self.meaning}', "
                f"description='{self.description}')")

    def setElement(self, element):
        self.element = element


#结合上下纯卦获得六十四卦的二进制
def combineDiagrams(shang, xia):
    return (xia.value << 3) | shang.value


class ESixtyFourDiagrams(Enum):
    Qian_Qian = combineDiagrams(EDiagrams.Qian, EDiagrams.Qian)  # 乾为天
    Kun_Kun = combineDiagrams(EDiagrams.Kun, EDiagrams.Kun)  # 坤为地
    Kan_Zhen = combineDiagrams(EDiagrams.Kan, EDiagrams.Zhen)  # 水雷屯
    Gen_Kan = combineDiagrams(EDiagrams.Gen, EDiagrams.Kan)  # 山水蒙
    Kan_Qian = combineDiagrams(EDiagrams.Kan, EDiagrams.Qian)  # 水天需
    Qian_Kan = combineDiagrams(EDiagrams.Qian, EDiagrams.Kan)  # 天水讼
    Kun_Kan = combineDiagrams(EDiagrams.Kun, EDiagrams.Kan)  # 地水师
    Kan_Kun = combineDiagrams(EDiagrams.Kan, EDiagrams.Kun)  # 水地比
    Xun_Qian = combineDiagrams(EDiagrams.Xun, EDiagrams.Qian)  # 风天小畜
    Qian_Dui = combineDiagrams(EDiagrams.Qian, EDiagrams.Dui)  # 天泽履
    Kun_Qian = combineDiagrams(EDiagrams.Kun, EDiagrams.Qian)  # 地天泰
    Qian_Kun = combineDiagrams(EDiagrams.Qian, EDiagrams.Kun)  # 天地否
    Qian_Li = combineDiagrams(EDiagrams.Qian, EDiagrams.Li)  # 天火同人
    Li_Qian = combineDiagrams(EDiagrams.Li, EDiagrams.Qian)  # 火天大有
    Kun_Gen = combineDiagrams(EDiagrams.Kun, EDiagrams.Gen)  # 地山谦
    Zhen_Kun = combineDiagrams(EDiagrams.Zhen, EDiagrams.Kun)  # 雷地豫
    Dui_Zhen = combineDiagrams(EDiagrams.Dui, EDiagrams.Zhen)  # 泽雷随
    Gen_Xun = combineDiagrams(EDiagrams.Gen, EDiagrams.Xun)  # 山风蛊
    Kun_Dui = combineDiagrams(EDiagrams.Kun, EDiagrams.Dui)  # 地泽临
    Xun_Kun = combineDiagrams(EDiagrams.Xun, EDiagrams.Kun)  # 风地观
    Li_Zhen = combineDiagrams(EDiagrams.Li, EDiagrams.Zhen)  # 火雷噬嗑
    Gen_Li = combineDiagrams(EDiagrams.Gen, EDiagrams.Li)  # 山火贲
    Gen_Kun = combineDiagrams(EDiagrams.Gen, EDiagrams.Kun)  # 山地剥
    Kun_Zhen = combineDiagrams(EDiagrams.Kun, EDiagrams.Zhen)  # 地雷复
    Qian_Zhen = combineDiagrams(EDiagrams.Qian, EDiagrams.Zhen)  # 天雷无妄
    Gen_Qian = combineDiagrams(EDiagrams.Gen, EDiagrams.Qian)  # 山天大畜
    Gen_Zhen = combineDiagrams(EDiagrams.Gen, EDiagrams.Zhen)  # 山雷颐
    Dui_Xun = combineDiagrams(EDiagrams.Dui, EDiagrams.Xun)  # 泽风大过
    Kan_Kan = combineDiagrams(EDiagrams.Kan, EDiagrams.Kan)  # 坎为水
    Li_Li = combineDiagrams(EDiagrams.Li, EDiagrams.Li)  # 离为火
    Dui_Gen = combineDiagrams(EDiagrams.Dui, EDiagrams.Gen)  # 泽山咸
    Zhen_Xun = combineDiagrams(EDiagrams.Zhen, EDiagrams.Xun)  # 雷风恒
    Qian_Gen = combineDiagrams(EDiagrams.Qian, EDiagrams.Gen)  # 天山遁
    Zhen_Qian = combineDiagrams(EDiagrams.Zhen, EDiagrams.Qian)  # 雷天大壮
    Li_Kun = combineDiagrams(EDiagrams.Li, EDiagrams.Kun)  # 火地晋
    Kun_Li = combineDiagrams(EDiagrams.Kun, EDiagrams.Li)  # 地火明夷
    Xun_Li = combineDiagrams(EDiagrams.Xun, EDiagrams.Li)  # 风火家人
    Li_Dui = combineDiagrams(EDiagrams.Li, EDiagrams.Dui)  # 火泽睽
    Kan_Gen = combineDiagrams(EDiagrams.Kan, EDiagrams.Gen)  # 水山蹇
    Zhen_Kan = combineDiagrams(EDiagrams.Zhen, EDiagrams.Kan)  # 雷水解
    Gen_Dui = combineDiagrams(EDiagrams.Gen, EDiagrams.Dui)  # 山泽损
    Xun_Zhen = combineDiagrams(EDiagrams.Xun, EDiagrams.Zhen)  # 风雷益
    Dui_Qian = combineDiagrams(EDiagrams.Dui, EDiagrams.Qian)  # 泽天夬
    Qian_Xun = combineDiagrams(EDiagrams.Qian, EDiagrams.Xun)  # 天风姤
    Dui_Kun = combineDiagrams(EDiagrams.Dui, EDiagrams.Kun)  # 泽地萃
    Kun_Xun = combineDiagrams(EDiagrams.Kun, EDiagrams.Xun)  # 地风升
    Dui_Kan = combineDiagrams(EDiagrams.Dui, EDiagrams.Kan)  # 泽水困
    Kan_Xun = combineDiagrams(EDiagrams.Kan, EDiagrams.Xun)  # 水风井
    Dui_Li = combineDiagrams(EDiagrams.Dui, EDiagrams.Li)  # 泽火革
    Li_Xun = combineDiagrams(EDiagrams.Li, EDiagrams.Xun)  # 火风鼎
    Zhen_Zhen = combineDiagrams(EDiagrams.Zhen, EDiagrams.Zhen)  # 震为雷
    Gen_Gen = combineDiagrams(EDiagrams.Gen, EDiagrams.Gen)  # 艮为山
    Xun_Gen = combineDiagrams(EDiagrams.Xun, EDiagrams.Gen)  # 风山渐
    Zhen_Dui = combineDiagrams(EDiagrams.Zhen, EDiagrams.Dui)  # 雷泽归妹
    Zhen_Li = combineDiagrams(EDiagrams.Zhen, EDiagrams.Li)  # 雷火丰
    Li_Gen = combineDiagrams(EDiagrams.Li, EDiagrams.Gen)  # 火山旅
    Xun_Xun = combineDiagrams(EDiagrams.Xun, EDiagrams.Xun)  # 巽为风
    Dui_Dui = combineDiagrams(EDiagrams.Dui, EDiagrams.Dui)  # 兑为泽
    Xun_Kan = combineDiagrams(EDiagrams.Xun, EDiagrams.Kan)  # 风水涣
    Kan_Dui = combineDiagrams(EDiagrams.Kan, EDiagrams.Dui)  # 水泽节
    Xun_Dui = combineDiagrams(EDiagrams.Xun, EDiagrams.Dui)  # 风泽中孚
    Zhen_Gen = combineDiagrams(EDiagrams.Zhen, EDiagrams.Gen)  # 雷山小过
    Kan_Li = combineDiagrams(EDiagrams.Kan, EDiagrams.Li)  # 水火既济
    Li_Kan = combineDiagrams(EDiagrams.Li, EDiagrams.Kan)  # 火水未济


sixty_four_diagrams_info = {
    ESixtyFourDiagrams.Qian_Qian: SixtyFourDiagramInfo(
        name="乾为天",
        statement="元亨利贞。",
        meaning="强健",
        description="乾卦象征强健和积极向上，代表创造力和领导力。",
        eDiagram=ESixtyFourDiagrams.Qian_Qian,
    ),
    ESixtyFourDiagrams.Kun_Kun: SixtyFourDiagramInfo(
        name="坤为地",
        statement="元亨，利牝马之贞。",
        meaning="顺从",
        description="坤卦象征顺从和包容，代表接纳和滋养。",
        eDiagram=ESixtyFourDiagrams.Kun_Kun,
    ),
    ESixtyFourDiagrams.Li_Li: SixtyFourDiagramInfo(
        name="离为火",
        statement="亨，柔蓉，故小人道而无行。",
        meaning="光明",
        description="离卦象征光明和分离，提醒保持清晰的目标。",
        eDiagram=ESixtyFourDiagrams.Li_Li,
    ),
    ESixtyFourDiagrams.Xun_Xun: SixtyFourDiagramInfo(
        name="巽为风",
        statement="亨，柔蓉，故小人道而无行。",
        meaning="顺应",
        description="巽卦象征风，表示适应变化的能力。",
        eDiagram=ESixtyFourDiagrams.Xun_Xun,
    ),
    ESixtyFourDiagrams.Dui_Dui: SixtyFourDiagramInfo(
        name="兑为泽",
        statement="亨，利贞。",
        meaning="喜悦",
        description="兑卦象征喜悦与交流，代表愉快的合作。",
        eDiagram=ESixtyFourDiagrams.Dui_Dui,
    ),
    ESixtyFourDiagrams.Zhen_Zhen: SixtyFourDiagramInfo(
        name="震为雷",
        statement="亨。震来虩虩，笑言哑哑。",
        meaning="震动",
        description="震卦象征雷电，表示动荡和惊恐的情景。",
        eDiagram=ESixtyFourDiagrams.Zhen_Zhen,
    ),
    ESixtyFourDiagrams.Gen_Gen: SixtyFourDiagramInfo(
        name="艮为山",
        statement="艮其背，不获其身。",
        meaning="止步",
        description="艮卦象征山，代表静止和克制。",
        eDiagram=ESixtyFourDiagrams.Gen_Gen,
    ),
    ESixtyFourDiagrams.Kan_Kan: SixtyFourDiagramInfo(
        name="坎为水",
        statement="亨，利贞。",
        meaning="危险",
        description="坎卦象征水，提醒小心谨慎，避免危险。",
        eDiagram=ESixtyFourDiagrams.Kan_Kan,
    ),
    ESixtyFourDiagrams.Li_Gen: SixtyFourDiagramInfo(
        name="火山旅",
        statement="亨，利贞，故小人之道。",
        meaning="旅行",
        description="旅卦象征旅行，表示探索新领域和自我发现。",
        eDiagram=ESixtyFourDiagrams.Li_Gen,
    ),
    ESixtyFourDiagrams.Kan_Li: SixtyFourDiagramInfo(
        name="水火既济",
        statement="亨，利贞。",
        meaning="相辅",
        description="既济卦象征相辅相成，表示和谐共生。",
        eDiagram=ESixtyFourDiagrams.Kan_Li,
    ),
    ESixtyFourDiagrams.Xun_Kan: SixtyFourDiagramInfo(
        name="风水涣",
        statement="亨，利见大人。",
        meaning="涣散",
        description="涣卦象征分散，提醒团结、理顺关系。",
        eDiagram=ESixtyFourDiagrams.Xun_Kan,
    ),
    ESixtyFourDiagrams.Dui_Gen: SixtyFourDiagramInfo(
        name="泽山咸",
        statement="亨，小畜之志。",
        meaning="困境",
        description="困卦象征困境，提醒应对困难和挫折。",
        eDiagram=ESixtyFourDiagrams.Dui_Gen,
    ),
    ESixtyFourDiagrams.Zhen_Gen: SixtyFourDiagramInfo(
        name="雷山小过",
        statement="亨，利贞。",
        meaning="小过",
        description="小过卦象征轻微失误，提醒稳中求进。",
        eDiagram=ESixtyFourDiagrams.Zhen_Gen,
    ),
    ESixtyFourDiagrams.Kun_Xun: SixtyFourDiagramInfo(
        name="地风升",
        statement="元亨，利见大人。",
        meaning="上升",
        description="升卦象征提升，表示通过奋斗取得进步。",
        eDiagram=ESixtyFourDiagrams.Kun_Xun,
    ),
    ESixtyFourDiagrams.Li_Kun: SixtyFourDiagramInfo(
        name="火地晋",
        statement="康侯用锡马蕃庶，昼日三接。",
        meaning="进步",
        description="晋卦象征进步，表示积极努力。",
        eDiagram=ESixtyFourDiagrams.Li_Kun,
    ),
    ESixtyFourDiagrams.Gen_Xun: SixtyFourDiagramInfo(
        name="山风蛊",
        statement="亨，利贞。",
        meaning="腐化",
        description="蛊卦象征治理，表示面对旧有问题和解决腐败。",
        eDiagram=ESixtyFourDiagrams.Gen_Xun,
    ),
    ESixtyFourDiagrams.Qian_Gen: SixtyFourDiagramInfo(
        name="天山遁",
        statement="亨，小利贞。",
        meaning="遁隐",
        description="遁卦象征退隐，表示隐忍和躲避。",
        eDiagram=ESixtyFourDiagrams.Qian_Gen,
    ),
    ESixtyFourDiagrams.Xun_Dui: SixtyFourDiagramInfo(
        name="风泽中孚",
        statement="豚鱼吉，利涉大川。",
        meaning="诚信",
        description="中孚卦象征诚实，表示言行一致、言出必行。",
        eDiagram=ESixtyFourDiagrams.Xun_Dui,
    ),
    ESixtyFourDiagrams.Dui_Li: SixtyFourDiagramInfo(
        name="泽火革",
        statement="己日乃孚，元亨利贞。",
        meaning="改革",
        description="革卦象征革新，表示摆脱旧事物、迎接新生。",
        eDiagram=ESixtyFourDiagrams.Dui_Li,
    ),
    ESixtyFourDiagrams.Zhen_Xun: SixtyFourDiagramInfo(
        name="雷风恒",
        statement="亨，无咎，利贞。",
        meaning="恒久",
        description="恒卦象征持久和坚定，提醒坚持不懈并有耐心。",
        eDiagram=ESixtyFourDiagrams.Zhen_Xun,
    ),
    ESixtyFourDiagrams.Kun_Gen: SixtyFourDiagramInfo(
        name="地山谦",
        statement="亨，君子有终。",
        meaning="谦虚",
        description="谦卦象征谦逊，提醒保持低调、包容和克己。",
        eDiagram=ESixtyFourDiagrams.Kun_Gen,
    ),
    ESixtyFourDiagrams.Dui_Qian: SixtyFourDiagramInfo(
        name="泽天夬",
        statement="亨，利见大人。",
        meaning="决断",
        description="夬卦象征果断，提醒做出明智决策。",
        eDiagram=ESixtyFourDiagrams.Dui_Qian,
    ),
    ESixtyFourDiagrams.Kun_Li: SixtyFourDiagramInfo(
        name="地火明夷",
        statement="利艰贞。",
        meaning="受难",
        description="明夷卦象征暗淡，提醒面对困境要保持冷静与坚韧。",
        eDiagram=ESixtyFourDiagrams.Kun_Li,
    ),
    ESixtyFourDiagrams.Qian_Li: SixtyFourDiagramInfo(
        name="天火同人",
        statement="亨，王假之。",
        meaning="团结",
        description="同人卦象征团结，强调合作与共赢。",
        eDiagram=ESixtyFourDiagrams.Qian_Li,
    ),
    ESixtyFourDiagrams.Zhen_Li: SixtyFourDiagramInfo(
        name="雷火丰",
        statement="亨，王假之。",
        meaning="丰盛",
        description="丰卦象征繁荣昌盛，表示丰收与成就。",
        eDiagram=ESixtyFourDiagrams.Zhen_Li,
    ),
    ESixtyFourDiagrams.Xun_Li: SixtyFourDiagramInfo(
        name="风火家人",
        statement="亨，王假之。",
        meaning="家庭",
        description="家人卦象征家庭和睦，代表温暖和支持。",
        eDiagram=ESixtyFourDiagrams.Xun_Li,
    ),
    ESixtyFourDiagrams.Zhen_Kun: SixtyFourDiagramInfo(
        name="雷地豫",
        statement="利建侯行师。",
        meaning="愉悦",
        description="豫卦象征愉悦，代表安心。",
        eDiagram=ESixtyFourDiagrams.Zhen_Kun,
    ),
    ESixtyFourDiagrams.Xun_Qian: SixtyFourDiagramInfo(
        name="风天小畜",
        statement="亨，利贞。",
        meaning="小有所蓄",
        description="小畜卦象征小有所蓄，提醒保持克制。",
        eDiagram=ESixtyFourDiagrams.Xun_Qian,
    ),
    ESixtyFourDiagrams.Gen_Qian: SixtyFourDiagramInfo(
        name="山天大畜",
        statement="亨，利贞。",
        meaning="大有所蓄",
        description="大畜卦象征大有所蓄，强调积累和资源管理。",
        eDiagram=ESixtyFourDiagrams.Gen_Qian,
    ),
    ESixtyFourDiagrams.Kan_Xun: SixtyFourDiagramInfo(
        name="水风井",
        statement="亨，利贞。",
        meaning="井水",
        description="井卦象征水源，代表滋养和支持。",
        eDiagram=ESixtyFourDiagrams.Kan_Xun,
    ),
    ESixtyFourDiagrams.Li_Xun: SixtyFourDiagramInfo(
        name="火风鼎",
        statement="亨，利贞。",
        meaning="鼎盛",
        description="鼎卦象征鼎盛与发展，表示持久的成就。",
        eDiagram=ESixtyFourDiagrams.Li_Xun,
    ),
    ESixtyFourDiagrams.Dui_Xun: SixtyFourDiagramInfo(
        name="泽风大过",
        statement="亨，利贞。",
        meaning="过量",
        description="大过卦象征过量，提醒适度与节制。",
        eDiagram=ESixtyFourDiagrams.Dui_Xun,
    ),
    ESixtyFourDiagrams.Qian_Xun: SixtyFourDiagramInfo(
        name="天风姤",
        statement="亨，利见大人。",
        meaning="随和",
        description="随卦象征随和，代表适应变化与接受。",
        eDiagram=ESixtyFourDiagrams.Qian_Xun,
    ),
    ESixtyFourDiagrams.Kan_Gen: SixtyFourDiagramInfo(
        name="水山蹇",
        statement="亨，利贞。",
        meaning="阻碍",
        description="蹇卦象征阻碍，提醒应对困难与挑战。",
        eDiagram=ESixtyFourDiagrams.Kan_Gen,
    ),
    ESixtyFourDiagrams.Li_Kan: SixtyFourDiagramInfo(
        name="火水未济",
        statement="亨，利贞。",
        meaning="未济",
        description="未济卦象征未完结，提醒保持耐心与准备。",
        eDiagram=ESixtyFourDiagrams.Li_Kan,
    ),
    ESixtyFourDiagrams.Xun_Gen: SixtyFourDiagramInfo(
        name="风山渐",
        statement="亨，利贞。",
        meaning="渐进",
        description="渐卦象征渐进，提醒稳步前行与逐步发展。",
        eDiagram=ESixtyFourDiagrams.Xun_Gen,
    ),
    ESixtyFourDiagrams.Li_Dui: SixtyFourDiagramInfo(
        name="火泽睽",
        statement="亨，利贞。",
        meaning="分裂",
        description="睽卦象征分裂，提醒寻求和谐与团结。",
        eDiagram=ESixtyFourDiagrams.Li_Dui,
    ),
    ESixtyFourDiagrams.Kan_Zhen: SixtyFourDiagramInfo(
        name="水雷屯",
        statement="亨，利贞。",
        meaning="屯有阻碍",
        description="屯卦象征阻碍，提醒人们在面对困难时要保持耐心和坚持。",
        eDiagram=ESixtyFourDiagrams.Kan_Zhen,
    ),
    ESixtyFourDiagrams.Gen_Kan: SixtyFourDiagramInfo(
        name="山水蒙",
        statement="亨，柔蓄而志行。",
        meaning="蒙昧",
        description="蒙卦象征蒙昧与学习，鼓励人们从错误中吸取教训，逐步成长。",
        eDiagram=ESixtyFourDiagrams.Gen_Kan,
    ),
    ESixtyFourDiagrams.Kan_Qian: SixtyFourDiagramInfo(
        name="水天需",
        statement="亨，利用行人。",
        meaning="需索",
        description="需卦象征需求，表示在紧急情况下要懂得适应环境，寻求帮助。",
        eDiagram=ESixtyFourDiagrams.Kan_Qian,
    ),
    ESixtyFourDiagrams.Qian_Kan: SixtyFourDiagramInfo(
        name="天水讼",
        statement="亨，故小人不利于大人。",
        meaning="讼争",
        description="讼卦象征争执，提醒人们在处理纷争时要保持公正和理智。",
        eDiagram=ESixtyFourDiagrams.Qian_Kan,
    ),
    ESixtyFourDiagrams.Kun_Kan: SixtyFourDiagramInfo(
        name="地水师",
        statement="亨，柔克刚。",
        meaning="师出",
        description="师卦象征进攻与行动，提醒人们在行动前应做好充分准备。",
        eDiagram=ESixtyFourDiagrams.Kun_Kan,
    ),
    ESixtyFourDiagrams.Kan_Kun: SixtyFourDiagramInfo(
        name="水地比",
        statement="亨，兄弟和而利。",
        meaning="比和",
        description="比卦象征和谐，强调团结与合作的重要性。",
        eDiagram=ESixtyFourDiagrams.Kan_Kun,
    ),
    ESixtyFourDiagrams.Qian_Dui: SixtyFourDiagramInfo(
        name="天泽履",
        statement="亨，利见小人。",
        meaning="履行",
        description="履卦象征行动与责任，强调在做出承诺后应履行自己的责任。",
        eDiagram=ESixtyFourDiagrams.Qian_Dui,
    ),
    ESixtyFourDiagrams.Kun_Qian: SixtyFourDiagramInfo(
        name="地天泰",
        statement="亨，天时利。",
        meaning="泰和",
        description="泰卦象征和谐与安定，表示大环境适合发展与合作。",
        eDiagram=ESixtyFourDiagrams.Kun_Qian,
    ),
    ESixtyFourDiagrams.Qian_Kun: SixtyFourDiagramInfo(
        name="天地否",
        statement="亨，天地不交。",
        meaning="否决",
        description="否卦象征隔绝与否定，提醒人们在冲突中保持冷静和理智。",
        eDiagram=ESixtyFourDiagrams.Qian_Kun,
    ),
    ESixtyFourDiagrams.Li_Qian: SixtyFourDiagramInfo(
        name="火天大有",
        statement="元亨。",
        meaning="大有",
        description="大有卦象征极大的成就与繁荣，强调德行的重要性，只有具备德行的人才能长久持有财富与地位。",
        eDiagram=ESixtyFourDiagrams.Li_Qian,
    ),
    ESixtyFourDiagrams.Dui_Zhen: SixtyFourDiagramInfo(
        name="泽雷随",
        statement="亨，柔和则志行。",
        meaning="随和",
        description="随卦象征随和，代表适应变化与接受。",
        eDiagram=ESixtyFourDiagrams.Dui_Zhen,
    ),
    ESixtyFourDiagrams.Kun_Dui: SixtyFourDiagramInfo(
        name="地泽临",
        statement="亨，利见贤人。",
        meaning="临近",
        description="临卦象征靠近，强调面对他人应保持谦和与真诚。",
        eDiagram=ESixtyFourDiagrams.Kun_Dui,
    ),
    ESixtyFourDiagrams.Xun_Kun: SixtyFourDiagramInfo(
        name="风地观",
        statement="亨，利见士。",
        meaning="观察",
        description="观卦象征观察与了解，提醒人们在行动前要仔细观察环境。",
        eDiagram=ESixtyFourDiagrams.Xun_Kun,
    ),
    ESixtyFourDiagrams.Li_Zhen: SixtyFourDiagramInfo(
        name="火雷噬嗑",
        statement="亨，利贞。",
        meaning="噬嗑",
        description="噬嗑卦象征解决与化解，表示在困境中寻找解决方案。",
        eDiagram=ESixtyFourDiagrams.Li_Zhen,
    ),
    ESixtyFourDiagrams.Gen_Li: SixtyFourDiagramInfo(
        name="山火贲",
        statement="亨，利见士。",
        meaning="装饰",
        description="贲卦象征美化与装饰，强调在生活中应注重外在与内在的和谐。",
        eDiagram=ESixtyFourDiagrams.Gen_Li,
    ),
    ESixtyFourDiagrams.Gen_Kun: SixtyFourDiagramInfo(
        name="山地剥",
        statement="亨，利贞。",
        meaning="剥落",
        description="剥卦象征损失与剥离，提醒人们在生活中要保持警惕，防止损失。",
        eDiagram=ESixtyFourDiagrams.Gen_Kun,
    ),
    ESixtyFourDiagrams.Kun_Zhen: SixtyFourDiagramInfo(
        name="地雷复",
        statement="亨，利贞。",
        meaning="复苏",
        description="复卦象征复苏与重生，表示在逆境中寻找机会与希望。",
        eDiagram=ESixtyFourDiagrams.Kun_Zhen,
    ),
    ESixtyFourDiagrams.Qian_Zhen: SixtyFourDiagramInfo(
        name="天雷无妄",
        statement="亨，利贞。",
        meaning="无妄",
        description="无妄卦象征意外与惊喜，提醒人们在生活中保持开放的心态。",
        eDiagram=ESixtyFourDiagrams.Qian_Zhen,
    ),
    ESixtyFourDiagrams.Gen_Zhen: SixtyFourDiagramInfo(
        name="山雷颐",
        statement="亨，利贞。",
        meaning="颐养",
        description="颐卦象征滋养与保护，强调对他人和自身的关爱与呵护。",
        eDiagram=ESixtyFourDiagrams.Gen_Zhen,
    ),
    ESixtyFourDiagrams.Zhen_Qian: SixtyFourDiagramInfo(
        name="雷天大壮",
        statement="亨，利见大人。",
        meaning="壮大",
        description="大壮卦象征壮大与增强，表示在适当的时机采取行动。",
        eDiagram=ESixtyFourDiagrams.Zhen_Qian,
    ),
    ESixtyFourDiagrams.Zhen_Kan: SixtyFourDiagramInfo(
        name="雷水解",
        statement="亨，利贞。",
        meaning="解脱",
        description="解卦象征解脱与释放，强调在困境中找到解脱的途径。",
        eDiagram=ESixtyFourDiagrams.Zhen_Kan,
    ),
    ESixtyFourDiagrams.Gen_Dui: SixtyFourDiagramInfo(
        name="山泽损",
        statement="亨，利见贤人。",
        meaning="损失",
        description="损卦象征损失与减少，提醒人们在决策时要慎重。",
        eDiagram=ESixtyFourDiagrams.Gen_Dui,
    ),
    ESixtyFourDiagrams.Xun_Zhen: SixtyFourDiagramInfo(
        name="风雷益",
        statement="亨，利见士。",
        meaning="益处",
        description="益卦象征增益与提升，表示在合适的时机采取行动能带来好处。",
        eDiagram=ESixtyFourDiagrams.Xun_Zhen,
    ),
    ESixtyFourDiagrams.Dui_Kun: SixtyFourDiagramInfo(
        name="泽地萃",
        statement="亨，利贞。",
        meaning="困扰",
        description="困卦象征困扰与局限，提醒人们在面对困境时要保持清醒和冷静。",
        eDiagram=ESixtyFourDiagrams.Dui_Kun,
    ),
    ESixtyFourDiagrams.Dui_Kan: SixtyFourDiagramInfo(
        name="泽水困",
        statement="亨，利贞。",
        meaning="困境",
        description="困境卦象征在绝境中要寻求突破，强调机智与灵活应对。",
        eDiagram=ESixtyFourDiagrams.Dui_Kan,
    ),
    ESixtyFourDiagrams.Zhen_Dui: SixtyFourDiagramInfo(
        name="雷泽归妹",
        statement="亨，利见大人。",
        meaning="归属",
        description="归妹卦象征归属与联合，强调在团体中应相互支持与帮助。",
        eDiagram=ESixtyFourDiagrams.Zhen_Dui,
    ),
    ESixtyFourDiagrams.Kan_Dui: SixtyFourDiagramInfo(
        name="水泽节",
        statement="亨，利贞。",
        meaning="节制",
        description="节卦象征节制与控制，提醒人们在生活中要懂得适可而止。",
        eDiagram=ESixtyFourDiagrams.Kan_Dui,
    )
}


#根据游魂卦的方法算卦宫
def calculateDiagramPalace():
    # 乾为金
    sixty_four_diagrams_info[ESixtyFourDiagrams.Qian_Qian].setElement(EElement.Metal)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Qian_Qian)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Metal)

    # 坤为土
    sixty_four_diagrams_info[ESixtyFourDiagrams.Kun_Kun].setElement(EElement.Earth)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Kun_Kun)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Earth)

    # 离为火
    sixty_four_diagrams_info[ESixtyFourDiagrams.Li_Li].setElement(EElement.Fire)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Li_Li)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Fire)

    # 巽为木
    sixty_four_diagrams_info[ESixtyFourDiagrams.Xun_Xun].setElement(EElement.Wood)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Xun_Xun)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Wood)

    # 兑为金
    sixty_four_diagrams_info[ESixtyFourDiagrams.Dui_Dui].setElement(EElement.Metal)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Dui_Dui)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Metal)

    # 震为木
    sixty_four_diagrams_info[ESixtyFourDiagrams.Zhen_Zhen].setElement(EElement.Wood)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Zhen_Zhen)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Wood)

    # 艮为土
    sixty_four_diagrams_info[ESixtyFourDiagrams.Gen_Gen].setElement(EElement.Earth)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Gen_Gen)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Earth)

    # 坎为水
    sixty_four_diagrams_info[ESixtyFourDiagrams.Kan_Kan].setElement(EElement.Water)
    diagrams = getYouHunDiagrams(ESixtyFourDiagrams.Kan_Kan)
    for diagram in diagrams:
        sixty_four_diagrams_info[diagram].setElement(EElement.Water)


def getYouHunDiagrams(origin):
    one = ESixtyFourDiagrams((origin.value ^ 0b100000))
    two = ESixtyFourDiagrams((one.value ^ 0b010000))
    three = ESixtyFourDiagrams((two.value ^ 0b001000))
    four = ESixtyFourDiagrams((three.value ^ 0b000100))
    five = ESixtyFourDiagrams((four.value ^ 0b000010))
    you_hun = ESixtyFourDiagrams((five.value ^ 0b000100))
    gui_hun = ESixtyFourDiagrams((you_hun.value ^ 0b111000))

    return [one, two, three, four, five, you_hun, gui_hun]


def getDiagramName(diagram):
    info = diagrams_info[diagram]
    if info:
        return info.name + "为" + info.meaning
    else:
        return False


def getSixtyFourDiagramName(diagram):
    if not sixty_four_diagrams_info.__contains__(diagram):
        return False
    info = sixty_four_diagrams_info[diagram]
    if info:
        return info.name
    else:
        return False


#将六十四卦分离为上下纯卦
def sepSixtyFourDiagrams(origin):
    shang = EDiagrams(origin.value & 0b000111)
    xia = EDiagrams((origin.value & 0b111000) >> 3)
    return shang, xia


#根据本卦获取互卦
def getHuDiagram(ben):
    shang = EDiagrams(ben.value >> 1 & 0b000111)
    xia = EDiagrams(ben.value >> 2 & 0b000111)
    return getSixtyFourDiagramFromTwo(shang, xia)


#根据本卦和爻动获取变卦
def getBianDiagram(ben, yao):
    y = rotate_right(0b000001, yao, 6)
    return ESixtyFourDiagrams(ben.value ^ y)


#二进制数循环右移
def rotate_right(value, bits, total_bits):
    return (value >> bits) | (value << (total_bits - bits) & ((1 << total_bits) - 1))


def getDiagramFromNum(number):
    n = number % 8
    return EDiagrams((8 - n) % 8)


def getSixtyFourDiagramFromTwo(shang, xia):
    return ESixtyFourDiagrams(combineDiagrams(shang, xia))


def getSixtyFourDiagramFromNum(number1, number2):
    return getSixtyFourDiagramFromTwo(getDiagramFromNum(number1), getDiagramFromNum(number2))


def getShiChenFromTime(time):
    return math.floor((time % 24 + 1) / 2 + 1)


#查询六十四卦的刑冲关系
def getRelationOfSixtyFourDiagrams(diagram):
    shang, xia = sepSixtyFourDiagrams(diagram)
    return diagrams_info[shang].getRelationWithOther(diagrams_info[xia])


def isDiagramsEmpty(diagram, emptyList):
    info = diagrams_info[diagram]
    for e in emptyList:
        for dizhi in info.dizhi:
            if dizhi == e:
                return True
    return False


#根据用的属性和全局属性看喜用
def handleElement(ti_info: ElementInfo, global_element):
    ti_element = ti_info.element
    sheng_wo_element = element_info[ti_element].who_generate_me
    count = 0
    for i in global_element:
        if i == ti_element or i == sheng_wo_element:
            count += 1

    xi = []
    ji = []
    if count == 1:
        #极弱，顺应，喜削弱自己的
        xi.append(ti_info.who_restrain_me)
        xi.append(ti_info.who_i_restrain)
        xi.append(ti_info.who_i_generate)
        ji.append(ti_info.who_generate_me)
    elif count <= 3:
        #弱，喜欢增强自己的
        xi.append(ti_info.who_generate_me)
        ji.append(ti_info.who_restrain_me)
        ji.append(ti_info.who_i_restrain)
        ji.append(ti_info.who_i_generate)
    elif count <= 5:
        #强，喜欢削弱自己的
        xi.append(ti_info.who_restrain_me)
        xi.append(ti_info.who_i_restrain)
        xi.append(ti_info.who_i_generate)
        ji.append(ti_info.who_generate_me)
    else:
        #极强，顺应，喜增强自己的
        xi.append(ti_info.who_generate_me)
        ji.append(ti_info.who_restrain_me)
        ji.append(ti_info.who_i_restrain)
        ji.append(ti_info.who_i_generate)

    result = ""
    result += "体为" + ti_info.name + "，"
    result += str(count) + "/7; "
    result += "喜："
    for x in xi:
        result += element_info[x].name + ","
    result += "; "
    result += "忌："
    for j in ji:
        result += element_info[j].name + ","
    result += ";\n"

    for ge in global_element:
        if ge in xi:
            result += "喜" + element_info[ge].name + ";"
            continue
        if ge in ji:
            result += "忌" + element_info[ge].name + ";"
            continue
        result += "同" + element_info[ge].name + ";"

    return result


# def main(number1: int, number2: int, time_shi: int, year: int, month: int, day: int) -> dict:
# def main(number1: int, number2: int, time_shi: int, time_ri_tian_gan: int, time_ri_di_zhi: int) -> dict:
def main(number1: int, number2: int, time_shi: int, json_str: str) -> dict:
    calculateDiagramPalace()

    json_data = json.loads(json_str)
    tgdz = json_data["干支日期"]
    time_ri = tgdz.split(" ")[2]
    str_ri_tian_gan = time_ri[0]
    str_ri_di_zhi = time_ri[1]
    # a = cnlunar.Lunar(datetime.datetime(2024, 11, 12, 10, 30), godType='8char')  # 常规算法
    # dayEight = a.day8Char
    time_ri_tian_gan = None
    time_ri_di_zhi = None
    for i in tian_gan_info:
        if tian_gan_info[i] == str_ri_tian_gan:
            time_ri_tian_gan = i
            break

    for i in dizhi_info:
        if dizhi_info[i] == str_ri_di_zhi:
            time_ri_di_zhi = i
            break

    # solar = Solar(year, month, day)
    # date = Converter().Solar2Lunar(solar)
    # lunar_year = date.year
    # lunar_month = date.month
    # lunar_day = date.day
    shi_chen = getShiChenFromTime(time_shi)
    kong_wang1, kong_wang2 = getKongWang(time_ri_tian_gan, time_ri_di_zhi)
    yao = (number1 + number2 + shi_chen) % 6

    #起卦
    ben = getSixtyFourDiagramFromNum(number1, number2)
    hu = getHuDiagram(ben)
    bian = getBianDiagram(ben, yao)

    #查询刑冲关系
    ben_xc = getRelationOfSixtyFourDiagrams(ben)
    ben_xc_result = ""
    for i in ben_xc:
        ben_xc_result += xing_chong_info[i]
    if ben_xc_result == "":
        ben_xc_result = "无"

    hu_xc = getRelationOfSixtyFourDiagrams(hu)
    hu_xc_result = ""
    for i in hu_xc:
        hu_xc_result += xing_chong_info[i]
    if hu_xc_result == "":
        hu_xc_result = "无"

    bian_xc = getRelationOfSixtyFourDiagrams(bian)
    bian_xc_result = ""
    for i in bian_xc:
        bian_xc_result += xing_chong_info[i]
    if bian_xc_result == "":
        bian_xc_result = "无"

    ben_shang, ben_xia = sepSixtyFourDiagrams(ben)
    hu_shang, hu_xia = sepSixtyFourDiagrams(hu)
    bian_shang, bian_xia = sepSixtyFourDiagrams(bian)

    #看属性
    elements = []
    elements.append(diagrams_info[ben_shang].element)
    elements.append(diagrams_info[ben_xia].element)
    elements.append(diagrams_info[hu_shang].element)
    elements.append(diagrams_info[hu_xia].element)
    elements.append(diagrams_info[bian_shang].element)
    elements.append(diagrams_info[bian_xia].element)
    elements_str = ""
    for e in elements:
        elements_str += element_info[e].name

    elements.append(sixty_four_diagrams_info[ben].element)
    ben_element_str = element_info[sixty_four_diagrams_info[ben].element].name

    if yao <= 3:
        ti_element = element_info[diagrams_info[ben_shang].element]
    else:
        ti_element = element_info[diagrams_info[ben_xia].element]
    ti_element_str = ti_element.name

    element_result_str = handleElement(ti_element, elements)

    #看空亡
    gua_kong_wang = ""
    if isDiagramsEmpty(ben_shang, [kong_wang1, kong_wang2]):
        gua_kong_wang += "本卦上卦空亡;"
    if isDiagramsEmpty(ben_xia, [kong_wang1, kong_wang2]):
        gua_kong_wang += "本卦下卦空亡;"
    if isDiagramsEmpty(hu_shang, [kong_wang1, kong_wang2]):
        gua_kong_wang += "互卦上卦空亡;"
    if isDiagramsEmpty(hu_xia, [kong_wang1, kong_wang2]):
        gua_kong_wang += "互卦下卦空亡;"
    if isDiagramsEmpty(bian_shang, [kong_wang1, kong_wang2]):
        gua_kong_wang += "变卦上卦空亡;"
    if isDiagramsEmpty(bian_xia, [kong_wang1, kong_wang2]):
        gua_kong_wang += "变卦下卦空亡;"

    if gua_kong_wang == "":
        gua_kong_wang = "无空亡"

    result = {
        "ben": getSixtyFourDiagramName(ben),
        "hu": getSixtyFourDiagramName(hu),
        "bian": getSixtyFourDiagramName(bian),
        "yao": yao == 0 and 6 or yao,
        "kong_wang": dizhi_info[kong_wang1] + dizhi_info[kong_wang2],
        "gua_kong_wang": gua_kong_wang,
        "ben_xc": ben_xc_result,
        "hu_xc": hu_xc_result,
        "bian_xc": bian_xc_result,
        "elements": elements_str,
        "ben_element": ben_element_str,
        "ti_element": ti_element_str,
        "element_result": element_result_str
    }
    print(result)

    return result

# json_str = "{\"公历日期\":\"2024年11月12日 星期二\",\"农历日期\":\"农历二零二四年 十月(大) 十二\",\"黄历日期\":\"阳历2024年11月12日，甲辰年阴历十月十二日\",\"回历日期\":\"伊斯兰历1446年5月10日\",\"干支日期\":\"甲辰年 乙亥月 庚辰日\",\"五行纳音\":\"白腊金\",\"值日星神\":\"司命（吉星）\",\"宜\":\"开光、解除、拆卸、翻新 修造、动土、安床、纳畜、安葬、启钻、入殓、\",\"忌\":\"结婚 嫁娶 开业 开幕 开市 出火 栽种 破土 动土 搬迁新宅 乔迁新居 入宅 搬家 移徙 安香 分家 分居 掘井 作灶\"}"
#
# main(1, 1, 10, json_str)
