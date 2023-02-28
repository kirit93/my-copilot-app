from enum import Enum, EnumMeta


'''
Generic Enums to enforce enum rules
'''
# https://stackoverflow.com/a/65225753


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass

###############################


class SupportedStyles(BaseEnum):
    STYLE_0n3p14c3v1 = "one_piece"
    STYLE_ch41ns4wv1 = "chain_saw"
    STYLE_dr4g0nb4llv1 = "dragon_ball_z"
    STYLE_m1h3r0v1 = "my_hero_academy"
    STYLE_p0k3m0nv1 = "pokemon"
    STYLE_4tt4ck0nt1t4nv1 = "attack_on_titan"
    STYLE_bl34chv1 = "bleach"
    STYLE_d3m0ns8lay3rv1 = "demon_slayer"
    STYLE_f4m1l1sp1v1 = "spy_x_family"
    STYLE_n4rut0v1 = "naruto"
    STYLE_r1ckm0rt1v1 = "rick_n_morty"
