import re
import sys
import time

bigrams = {'aa': ['l', 'z', 'k', 'b', 'r'], 'ab': 1, 'ac': 1, 'ad': 1, 'ae':
['a', 'c', 'f', 's', 'l', 'd', 'g', 'e', 'b', 'h', 'k',
'v', 'i', 't', 'm', 'r', 'n', 'p'], 'af': ['c', 'f', 'l',
'w', 'o', 'd', 'e', 'g', 'h', 'b', 'k', 'm', 't', 'r',
'n', 'u', 's'], 'ag': 1, 'ah': ['a', 'z', 'd', 'e', 'h', 'k',
'r', 'j', 'c', 'l', 'i', 't', 'v', 'n', 'g', 'b', 'm',
'p', 'y', 'f', 'u', 's'], 'ai': 1, 'aj': ['c', 'f', 'h', 'm',
'r', 'p'], 'ak': 1, 'al': 1, 'am': 1, 'an': 1, 'ao': ['c', 'k', 'b',
'h', 'i', 'r'], 'ap': 1, 'aq': ['c', 'l', 'b', 'v', 'r',
'p'], 'ar': 1, 'as': 1, 'at': 1, 'au': 1, 'av': 1, 'aw': ['d', 'e',
'h', 'k', 'r', 'c', 'j', 'l', 't', 'n', 'g', 'b', 'm',
'p', 'y', 'f', 'w', 'u', 's'], 'ax': ['f', 'l', 'w', 'o',
'e', 'k', 'm', 't', 'r', 's'], 'ay': 1, 'az': ['j', 'f', 'l',
'z', 'd', 'g', 'e', 'h', 'k', 'b', 'i', 'm', 't', 'r',
'n', 'p'], 'ba': 1, 'bb': ['a', 'y', 'o', 'e', 'i', 'm',
'u'], 'bc': ['o', 'u'], 'bd': ['a', 'y', 'o', 'm', 'u'], 'be':
1, 'bf': ['a', 'o', 'e', 'm', 'u'], 'bg': ['o', 'a', 'u'],
'bh': ['a', 'o', 'u'], 'bi': 1, 'bj': ['o', 'a', 'u'], 'bk':
['m'], 'bl': 1, 'bm': ['m', 'u'], 'bn': ['a', 'o', 'i', 'm',
'u'], 'bo': 1, 'bp': ['m', 'u'], 'bq': 0, 'br': 1, 'bs': ['a', 'l',
'o', 'e', 'b', 'i', 'm', 't', 'r', 'u'], 'bt': ['o', 'm',
'e', 'u'], 'bu': 1, 'bv': ['o', 'u'], 'bw': ['a', 'l', 'o',
'm', 'r', 'u'], 'bx': 0, 'by': ['a', 'y', 'l', 'o', 'd', 'g',
'e', 'b', 'i', 'm', 'r', 'u', 's'], 'bz': ['u'], 'ca': 1, 'cb':
0, 'cc': ['a', 'o', 'e', 'i', 'u'], 'cd': ['e'], 'ce': 1, 'cf': 0,
'cg': 0, 'ch': 1, 'ci': 1, 'cj': 0, 'ck': 1, 'cl': 1, 'cm': ['a', 'n'],
'cn': ['a', 'i'], 'co': 1, 'cp': ['r'], 'cq': ['a', 'e'], 'cr': 1,
'cs': ['a', 'o', 'e', 'i', 'r', 'n', 's'], 'ct': 1, 'cu': 1,
'cv': 0, 'cw': 0, 'cx': 0, 'cy': ['a', 'c', 'l', 'o', 'e', 'i',
't', 'r', 'n', 'u', 's'], 'cz': ['e'], 'da': 1, 'db': ['a',
'l', 'o', 'd', 'e', 'i', 'r', 'n', 'u'], 'dc': ['a', 'l',
'o', 'e', 'r', 'n'], 'dd': ['a', 'o', 'e', 'i', 'n', 'u'],
'de': 1, 'df': ['a', 'l', 'o', 'd', 'e', 'i', 'r', 'n', 'u'],
'dg': ['a', 'l', 'o', 'e', 'i', 'n', 'u'], 'dh': ['a', 'l',
'o', 'e', 'i', 'r', 'n', 'u'], 'di': 1, 'dj': ['a', 'n'], 'dk':
['o', 'n', 'e'], 'dl': ['a', 'l', 'w', 'o', 'd', 'e', 'i',
'r', 'n', 'u'], 'dm': ['a', 'l', 'o', 'd', 'e', 'i', 'r',
'n', 'u'], 'dn': ['a', 'l', 'w', 'o', 'd', 'e', 'i', 'r',
'n', 'u'], 'do': 1, 'dp': ['a', 'l', 'o', 'e', 'i', 'v', 'r',
'n', 'u'], 'dq': ['a', 'n', 'h'], 'dr': 1, 'ds': 1, 'dt': ['a',
'o', 'e', 'i', 'r', 'n'], 'du': 1, 'dv': ['a', 'r'], 'dw':
['a', 'l', 'o', 'e', 'i', 'r', 'n'], 'dx': 0, 'dy': ['a',
'l', 'w', 'o', 'd', 'e', 'i', 'r', 'n', 'u'], 'dz': ['a',
'u'], 'ea': 1, 'eb': ['z', 'd', 'e', 'k', 'h', 'r', 'c', 'l',
'i', 't', 'v', 'n', 's', 'g', 'b', 'm', 'y', 'f', 'w',
'o', 'u', 'p'], 'ec': 1, 'ed': 1, 'ee': 1, 'ef': 1, 'eg': 1, 'eh':
['c', 'l', 'o', 'd', 'e', 'g', 'b', 'k', 'v', 'm', 't',
'r', 'n', 'u', 's'], 'ei': ['z', 'd', 'e', 'h', 'k', 'r',
'c', 'l', 'i', 't', 'v', 'n', 'g', 'b', 'm', 'p', 'f',
'y', 'w', 'o', 'u', 's'], 'ej': ['j', 'l', 'd', 'e', 'b',
'r', 'u', 'p'], 'ek': ['c', 'f', 's', 'l', 'd', 'e', 'h',
'b', 'i', 'm', 't', 'r', 'p'], 'el': 1, 'em': 1, 'en': 1, 'eo':
['a', 'j', 'y', 's', 'c', 'l', 'z', 'd', 'g', 'h', 'k',
'v', 'm', 't', 'r', 'n', 'u', 'p'], 'ep': 1, 'eq': ['l', 'o',
'd', 'e', 'b', 'h', 't', 'r', 'n', 's'], 'er': 1, 'es': 1,
'et': 1, 'eu': ['c', 'f', 'y', 'l', 'o', 'd', 'x', 'g', 'p',
'h', 'k', 'i', 'm', 't', 'r', 'n', 'u', 's'], 'ev': 1, 'ew':
['z', 'd', 'e', 'h', 'k', 'r', 'j', 'c', 'l', 'i', 't',
'v', 'n', 'g', 'b', 'm', 'p', 'f', 'y', 's'], 'ex': 1, 'ey':
['c', 'f', 's', 'y', 'l', 'o', 'g', 'k', 'b', 'h', 'v',
'm', 't', 'r', 'n', 'u', 'p'], 'ez': ['f', 'd', 'e', 'b',
'i', 'm', 'r', 'u', 'p'], 'fa': 1, 'fb': ['f', 'l', 'o', 'e',
'r'], 'fc': ['e'], 'fd': ['e', 'r'], 'fe': 1, 'ff': 1, 'fg': ['a',
'm'], 'fh': ['f', 'l'], 'fi': 1, 'fj': 0, 'fk': 0, 'fl': 1, 'fm':
['l'], 'fn': ['a', 'o', 'f', 'e'], 'fo': 1, 'fp': ['f', 'l'],
'fq': 0, 'fr': 1, 'fs': ['a', 'f', 'l', 'o', 'e', 'i', 'r',
'u'], 'ft': ['a', 'f', 'l', 'o', 'e', 'i', 'u'], 'fu': 1, 'fv':
0, 'fw': ['l'], 'fx': 0, 'fy': ['a', 'f', 'o', 'e', 'i', 'm',
'r', 's'], 'fz': 0, 'ga': 1, 'gb': ['a', 'o', 'e', 'g', 'n',
'u'], 'gc': ['o', 'g'], 'gd': ['y', 'n'], 'ge': 1, 'gf': ['a',
'o', 'n', 'u'], 'gg': ['a', 'o', 'e', 'i', 'n', 'u'], 'gh':
1, 'gi': 1, 'gj': ['o'], 'gk': 0, 'gl': 1, 'gm': ['a', 'y', 'o', 'd',
'e', 'i', 'n', 'u'], 'gn': ['a', 'y', 'o', 'g', 'e', 'i',
'r', 'n', 'u'], 'go': 1, 'gp': ['a', 'i', 'n', 'g'], 'gq': 0,
'gr': 1, 'gs': ['a', 'o', 'e', 'g', 'i', 'r', 'n', 'u'], 'gt':
['a', 'o', 'h', 'i', 'n'], 'gu': 1, 'gv': 0, 'gw': ['a', 'o',
'e', 'h', 'i', 'n', 'u'], 'gx': 0, 'gy': ['a', 'l', 'o', 'd',
'g', 'e', 'i', 'r', 'n'], 'gz': ['i'], 'ha': 1, 'hb': ['c',
't', 'g', 's'], 'hc': ['a', 'c', 'g', 't', 's'], 'hd': ['c',
't', 's'], 'he': 1, 'hf': ['c', 'g', 't', 'v', 'u', 's'], 'hg':
['c', 'g', 's'], 'hh': ['c', 't', 'g', 's'], 'hi': 1, 'hj': 0,
'hk': ['c', 's'], 'hl': ['a', 'c', 's', 'o', 'g', 't', 'p'],
'hm': ['o', 'c', 't', 's'], 'hn': ['a', 'c', 'o', 'g', 't',
's'], 'ho': 1, 'hp': ['c', 'd', 'g', 't', 's'], 'hq': ['t'],
'hr': ['c', 's', 'e', 'g', 't', 'u', 'p'], 'hs': ['a', 'c',
's', 'o', 'd', 'g', 'k', 't', 'p'], 'ht': 1, 'hu': ['a', 'c',
'w', 'o', 'd', 'x', 'p', 'e', 'g', 'b', 'i', 't', 'r',
'n', 's'], 'hv': 0, 'hw': ['c', 't', 'g', 's'], 'hx': 0, 'hy':
['c', 's', 'w', 'o', 'g', 'e', 't', 'r', 'n', 'p'], 'hz':
0, 'ia': 1, 'ib': 1, 'ic': 1, 'id': 1, 'ie': 1, 'if': 1, 'ig': 1, 'ih': ['j',
'l', 'd', 'h', 't', 'r', 'n'], 'ii': ['a', 'd', 'x', 'k',
'b', 'i', 'v', 'r', 'n', 'p'], 'ij': ['r', 'm', 'b', 'h'],
'ik': ['a', 'y', 'l', 'o', 'd', 'e', 'b', 'h', 'k', 'v',
'm', 't', 'r', 'n', 'p'], 'il': 1, 'im': 1, 'in': 1, 'io': 1, 'ip':
1, 'iq': ['a', 'l', 'p', 'b', 'm', 't', 'r', 'n', 's'], 'ir':
1, 'is': 1, 'it': 1, 'iu': ['c', 's', 'l', 'z', 'd', 'b', 'h',
'v', 'm', 't', 'r', 'n', 'u', 'p'], 'iv': 1, 'iw': ['l', 'x',
'd', 'b', 'k', 'm', 't', 'r'], 'ix': ['f', 's', 'l', 'w',
'x', 'd', 'm', 'v', 'r', 'n', 'u', 'p'], 'iy': ['l', 'k',
'b', 'm', 't', 'r'], 'iz': 1, 'ja': ['a', 'y', 'd', 'e', 'g',
'k', 'i', 't', 'r', 'n', 'u', 'p'], 'jb': 0, 'jc': 0, 'jd': 0,
'je': ['a', 'j', 'o', 'd', 'e', 'b', 'm', 'r', 'n'], 'jf': 0,
'jg': 0, 'jh': 0, 'ji': ['a', 'j', 'e', 'n', 'u'], 'jj': ['a'],
'jk': 0, 'jl': 0, 'jm': 0, 'jn': 0, 'jo': ['a', 'f', 'l', 'w', 'o',
'd', 'e', 'b', 'i', 'r', 'n', 's'], 'jp': 0, 'jq': 0, 'jr': 0,
'js': 0, 'jt': 0, 'ju': ['a', 'w', 'd', 'e', 'b', 'i', 'r',
'n', 'u', 's'], 'jv': 0, 'jw': 0, 'jx': 0, 'jy': 0, 'jz': 0, 'ka':
['a', 'c', 'l', 'o', 'd', 'e', 'k', 'h', 'i', 'r', 'n',
'u', 's'], 'kb': ['c', 'l', 'o', 'e', 'r', 'n'], 'kc': ['o',
'c', 'n'], 'kd': ['a', 'c', 'e', 'i', 'r'], 'ke': 1, 'kf':
['a', 'c', 'n', 'r'], 'kg': ['c', 'n', 'p'], 'kh': ['a', 'c',
'l', 'o', 'i', 'm', 'r', 'n'], 'ki': 1, 'kj': ['c'], 'kk':
['a', 'c', 'o', 'e', 'r', 'u'], 'kl': ['a', 'c', 'l', 'w',
'o', 'e', 'r', 'n', 'u', 's'], 'km': ['c', 'l', 'o', 'r',
'n', 's'], 'kn': ['a', 'c', 's', 'o', 'e', 'k', 'i', 't',
'r', 'n', 'p'], 'ko': ['a', 'c', 'l', 'o', 'e', 'r', 'n',
'u', 's'], 'kp': ['o', 'c', 'a', 'r'], 'kq': 0, 'kr': ['a',
'c', 'o', 'z', 'r', 'n', 's'], 'ks': ['a', 'c', 'l', 'w',
'o', 'e', 'i', 'm', 'r', 'n', 'u', 's'], 'kt': ['a', 'c',
'l', 'p', 'e', 'i', 'r', 'n', 's'], 'ku': ['a', 'c', 'o',
'i', 'r', 'n', 'u', 's'], 'kv': 0, 'kw': ['a', 'c', 'l', 'w',
'o', 'r', 'n', 'p'], 'kx': 0, 'ky': ['a', 'c', 'l', 'w', 'o',
'e', 'i', 'r', 'n', 'u', 's'], 'kz': 0, 'la': 1, 'lb': ['a',
'l', 'o', 'e', 'i', 'u'], 'lc': ['a', 'l', 'o', 'e', 'i',
'u'], 'ld': 1, 'le': 1, 'lf': 1, 'lg': ['a', 'l', 'o', 'e', 'i',
'u'], 'lh': ['l', 'o', 'e', 'i', 'r'], 'li': 1, 'lj': ['l'],
'lk': ['a', 'o', 'e', 'i', 'u'], 'll': 1, 'lm': ['a', 'l', 'o',
'e', 'i', 'u'], 'ln': ['a', 'l', 'o', 'e', 'i', 'u'], 'lo':
1, 'lp': ['a', 'y', 'l', 'o', 'e', 'i', 'r', 'u'], 'lq':
['a', 'i'], 'lr': ['a', 'l', 'o', 'e', 'h', 'i', 'u'], 'ls':
1, 'lt': 1, 'lu': 1, 'lv': ['a', 'y', 'o', 'e', 'b', 'i', 'u'],
'lw': ['a', 'l', 'o', 'e', 'i', 'r', 'u'], 'lx': 0, 'ly': 1,
'lz': 0, 'ma': 1, 'mb': 1, 'mc': ['a', 'o', 'e', 'i', 'r', 'u'],
'md': ['u'], 'me': 1, 'mf': ['a', 'o', 'e', 'i', 'r', 'u'], 'mg':
0, 'mh': ['o', 'u', 'r'], 'mi': 1, 'mj': ['a'], 'mk': ['y'], 'ml':
['a', 'l', 'o', 'e', 'i', 'r', 'u'], 'mm': 1, 'mn': ['a',
'y', 'l', 'o', 'e', 'i', 'r', 'u'], 'mo': 1, 'mp': 1, 'mq':
['u'], 'mr': ['a', 'i', 'o', 'r'], 'ms': ['a', 'y', 'l', 'o',
'e', 'g', 'h', 'i', 'r', 'u', 's'], 'mt': ['a', 'o', 'l',
'r'], 'mu': ['a', 'y', 'o', 'p', 'e', 'h', 'i', 'm', 't',
'r', 'n', 'u', 's'], 'mv': ['u'], 'mw': ['a', 'i', 'e', 'r'],
'mx': 0, 'my': ['a', 'y', 'l', 'o', 'e', 'g', 'i', 'm', 'r',
'u'], 'mz': 0, 'na': 1, 'nb': ['a', 'w', 'o', 'e', 'g', 'i',
'm', 'r', 'u'], 'nc': 1, 'nd': 1, 'ne': 1, 'nf': ['a', 'y', 'w',
'o', 'e', 'i', 'r', 'u'], 'ng': 1, 'nh': ['a', 'w', 'o', 'e',
'i', 'u'], 'ni': 1, 'nj': ['a', 'o', 'e', 'i', 'u'], 'nk':
['a', 'o', 'e', 'i', 'r', 'n', 'u'], 'nl': ['a', 'w', 'o',
'e', 'g', 'i', 'm', 'r', 'u'], 'nm': ['w', 'o', 'e', 'g',
'i', 'r', 'u'], 'nn': 1, 'no': 1, 'np': ['a', 'w', 'o', 'e',
'g', 'i', 't', 'r', 'u'], 'nq': ['a', 'o', 'e', 'i', 'u'],
'nr': ['a', 'w', 'o', 'e', 'i', 'r', 'u'], 'ns': 1, 'nt': 1,
'nu': ['a', 'l', 'w', 'o', 'd', 'e', 'g', 'k', 'b', 'h',
'i', 'm', 't', 'r', 'n', 'u', 's'], 'nv': ['a', 'o', 'e',
'i', 'u'], 'nw': ['a', 'w', 'o', 'e', 'i', 'u'], 'nx': ['a',
'i', 'y'], 'ny': ['a', 'y', 'w', 'o', 'e', 'i', 'm', 'r',
'n', 'u'], 'nz': ['o', 'a', 'e', 'u'], 'oa': 1, 'ob': ['a',
'd', 'x', 'h', 'r', 'c', 'j', 'l', 'i', 't', 'n', 'g',
'b', 'm', 'f', 'y', 'w', 'o', 's'], 'oc': 1, 'od': 1, 'oe':
['z', 'd', 'e', 'h', 'k', 'r', 'j', 'c', 'l', 'i', 't',
'n', 'g', 'b', 'm', 'p', 'f', 'y', 'w', 'o', 's'], 'of': 1,
'og': 1, 'oh': ['a', 'j', 'c', 'l', 'o', 'z', 'k', 'b', 'm',
'r', 'n', 's'], 'oi': 1, 'oj': ['j', 'b', 't', 'r', 's'], 'ok':
['a', 'c', 'j', 'y', 'l', 'w', 'o', 'h', 'b', 'v', 'm',
't', 'r', 'p'], 'ol': 1, 'om': 1, 'on': 1, 'oo': 1, 'op': 1, 'oq':
['c', 't', 'l', 'r'], 'or': 1, 'os': 1, 'ot': 1, 'ou': 1, 'ov': 1,
'ow': 1, 'ox': ['c', 'f', 's', 'l', 'd', 'b', 'k', 'i', 'm',
't', 'r', 'n', 'p'], 'oy': ['c', 'j', 'f', 'l', 'd', 'g',
'b', 'h', 'v', 't', 'r', 'n', 'u', 's'], 'oz': ['c', 'l',
'o', 'd', 'b', 'm', 't', 'r', 'n', 's'], 'pa': 1, 'pb': ['a',
'e', 'i', 'm', 'u', 's'], 'pc': ['o', 'i', 'e', 'u'], 'pd':
['a', 'c', 'o', 'e', 'm', 'u'], 'pe': 1, 'pf': ['a', 'l',
'o', 'e', 'i', 'm', 'u'], 'pg': ['o', 'm', 'u'], 'ph': 1, 'pi':
1, 'pj': ['a'], 'pk': ['a', 'o', 'i', 'm', 'n', 'u'], 'pl': 1,
'pm': ['a', 'l', 'w', 'o', 'e', 'i', 'm', 'r', 'u', 'p'],
'pn': ['a', 'y', 'o', 'e', 'i', 'm', 'r', 's'], 'po': 1, 'pp':
1, 'pq': 0, 'pr': 1, 'ps': ['a', 'c', 'f', 'y', 'l', 'w', 'o',
'p', 'e', 'b', 'i', 'm', 'r', 'u', 's'], 'pt': ['a', 'c',
'y', 'l', 'o', 'd', 'e', 'h', 'i', 'm', 'r', 'u'], 'pu': 1,
'pv': 0, 'pw': ['a', 'l', 'o', 'e', 'i', 'u'], 'px': 0, 'py':
['a', 's', 'l', 'o', 'e', 'i', 'm', 'r', 'u', 'p'], 'pz':
0, 'qa': 0, 'qb': 0, 'qc': 0, 'qd': 0, 'qe': 0, 'qf': 0, 'qg': 0, 'qh': 0,
'qi': 0, 'qj': 0, 'qk': 0, 'ql': 0, 'qm': 0, 'qn': 0, 'qo': 0, 'qp': 0, 'qq':
['s'], 'qr': ['d'], 'qs': 0, 'qt': 0, 'qu': 1, 'qv': 0, 'qw': 0, 'qx': 0,
'qy': 0, 'qz': 0, 'ra': 1, 'rb': ['a', 'o', 'e', 'i', 'u'], 'rc': 1,
'rd': 1, 're': 1, 'rf': ['a', 'y', 'o', 'e', 'i', 'u'], 'rg':
['a', 'o', 'e', 'i', 'u'], 'rh': ['a', 'o', 'e', 'i', 'r',
'n'], 'ri': 1, 'rj': ['o', 'a', 'e'], 'rk': ['a', 'o', 'e',
'i', 'u'], 'rl': 1, 'rm': 1, 'rn': 1, 'ro': 1, 'rp': ['a', 'o', 'e',
'i', 'u'], 'rq': ['a', 'o', 'e', 'i', 'u'], 'rr': 1, 'rs': 1,
'rt': 1, 'ru': 1, 'rv': ['a', 'o', 'e', 'i', 'u'], 'rw': ['a',
'i', 'e', 'o'], 'rx': 0, 'ry': 1, 'rz': ['o', 'a', 'e', 'u'],
'sa': 1, 'sb': ['a', 'w', 'o', 'e', 'g', 'i', 'r', 'u', 's'],
'sc': 1, 'sd': ['w', 'e', 'i', 'm', 'n'], 'se': 1, 'sf': ['y',
'w', 'e', 'i', 'n', 's'], 'sg': ['w', 'o', 'e', 'g', 'k',
'i', 'n'], 'sh': 1, 'si': 1, 'sj': ['i'], 'sk': ['a', 'f', 'l',
'o', 'd', 'p', 'e', 'g', 'k', 'b', 'h', 'i', 'm', 't',
'r', 'n', 'u', 's'], 'sl': 1, 'sm': 1, 'sn': ['a', 'e', 'k',
'i', 'r', 'n', 'u', 's'], 'so': 1, 'sp': 1, 'sq': ['a', 'o',
'e', 'i', 'r', 'u', 'p'], 'sr': ['i', 's', 'e', 'w'], 'ss':
1, 'st': 1, 'su': 1, 'sv': ['n'], 'sw': ['a', 'y', 's', 'w', 'x',
'd', 'e', 'g', 'b', 'i', 't', 'r', 'n', 'p'], 'sx': 0, 'sy':
['a', 'y', 'l', 'w', 'o', 'd', 'p', 'e', 'k', 'b', 'i',
'm', 't', 'r', 'n', 'u', 's'], 'sz': 0, 'ta': 1, 'tb': ['a',
'f', 'l', 'o', 'x', 'p', 'e', 'h', 'i', 'r', 'n', 'u',
's'], 'tc': ['a', 'l', 'o', 'p', 'e', 'h', 'i', 'r', 'n',
'u', 's'], 'td': ['l', 'e', 'h', 'n', 'u', 's'], 'te': 1, 'tf':
['a', 'c', 'l', 'o', 'e', 'b', 'h', 'i', 'r', 'n', 'u',
's'], 'tg': ['a', 'o', 'h', 'i', 'm', 'r', 'n', 'u', 's'],
'th': 1, 'ti': 1, 'tj': ['i'], 'tk': ['a', 'o', 'e'], 'tl': 1, 'tm':
['a', 'c', 'f', 'l', 'o', 'e', 'h', 'i', 'r', 'n', 'u',
's'], 'tn': ['a', 'c', 'f', 's', 'o', 'e', 'h', 'i', 't',
'r', 'n', 'u', 'p'], 'to': 1, 'tp': ['a', 'f', 'l', 'o', 'e',
'h', 'i', 'u', 's'], 'tq': 0, 'tr': 1, 'ts': 1, 'tt': 1, 'tu': 1, 'tv':
['u'], 'tw': 1, 'tx': 0, 'ty': 1, 'tz': ['a', 'l', 'e', 'i', 'r',
'n', 'u'], 'ua': 1, 'ub': 1, 'uc': 1, 'ud': ['a', 'c', 'j', 's',
'f', 'l', 'o', 'd', 'x', 'e', 'b', 'h', 'k', 'm', 't',
'r', 'n', 'p'], 'ue': 1, 'uf': ['a', 'c', 'f', 's', 'l', 'o',
'd', 'g', 'b', 'h', 'm', 't', 'r', 'n', 'p'], 'ug': 1, 'uh':
['o', 'f', 'h'], 'ui': 1, 'uj': ['j', 'l'], 'uk': ['a', 'j',
'y', 's', 'l', 'o', 'd', 'e', 'b', 'h', 'm', 'r', 'n',
'p'], 'ul': 1, 'um': 1, 'un': 1, 'uo': ['q', 'c', 'l', 'd', 'g',
'b', 't', 'r', 'n', 's'], 'up': 1, 'uq': ['o', 't'], 'ur': 1,
'us': 1, 'ut': 1, 'uu': ['c', 'm', 'd', 'n'], 'uv': ['a', 'j',
'l', 'o', 'd', 'g', 'e', 'r'], 'uw': ['r'], 'ux': ['a', 'j',
'l', 'o', 'b', 't', 'r'], 'uy': ['q', 'g', 'b'], 'uz': ['a',
'c', 'f', 's', 'o', 'g', 'b', 'h', 'm', 'n', 'p'], 'va': 1,
'vb': 0, 'vc': 0, 'vd': ['a', 'l'], 've': 1, 'vf': 0, 'vg': ['a'], 'vh':
0, 'vi': 1, 'vj': 0, 'vk': 0, 'vl': ['a'], 'vm': 0, 'vn': 0, 'vo': ['a',
'l', 'o', 'z', 'd', 'e', 'i', 't', 'r', 'n'], 'vp': 0, 'vq':
0, 'vr': ['e', 'u'], 'vs': ['a', 'i', 'e', 'u'], 'vt': ['o',
'd', 'p'], 'vu': ['a', 'l', 'o', 'e', 'i', 'n', 'u'], 'vv':
['a', 'i', 'e', 'o'], 'vw': 0, 'vx': 0, 'vy': ['a', 'o', 'e',
'i', 'v', 'r', 'n'], 'vz': 0, 'wa': 1, 'wb': ['o', 'a', 'e'],
'wc': ['o', 'e'], 'wd': ['a', 'o', 'f', 'e'], 'we': 1, 'wf':
['a', 'o', 'e'], 'wg': ['o', 'a', 'e'], 'wh': ['a', 'y', 'l',
'o', 'e', 'g', 'b', 'k', 'h', 't', 'r', 'n'], 'wi': 1, 'wj':
['o'], 'wk': ['a'], 'wl': ['o', 'a', 'e'], 'wm': ['o', 'a',
'e'], 'wn': ['a', 'o', 'e'], 'wo': 1, 'wp': ['a', 'o', 't',
'e'], 'wq': 0, 'wr': ['a', 'y', 's', 'l', 'o', 'd', 'e', 'g',
't', 'r', 'n', 'p'], 'ws': ['o', 'a', 'e'], 'wt': ['o', 'c',
'e', 'a'], 'wu': ['o', 'g', 'k', 't', 'r', 's'], 'wv': 0, 'ww':
['o', 'e'], 'wx': 0, 'wy': ['a', 'o', 'e', 'g', 'k', 'h'],
'wz': ['o'], 'xa': ['a', 'i', 'e'], 'xb': ['o'], 'xc': ['o',
'e'], 'xd': 0, 'xe': ['a', 'y', 'o', 'e', 'i', 'n', 'u'], 'xf':
['o', 'i', 'e'], 'xg': ['o'], 'xh': ['o', 'e'], 'xi': ['a',
'y', 'o', 'x', 'e', 'i', 'n', 'u'], 'xj': 0, 'xk': 0, 'xl':
['a', 'o', 'i', 'e'], 'xm': ['a'], 'xn': ['a'], 'xo': ['a',
'y', 'o', 'e', 'i', 'u'], 'xp': ['a', 'i', 'e'], 'xq': ['e'],
'xr': ['o'], 'xs': ['o', 'b'], 'xt': ['o', 'i', 'e', 'u'], 'xu':
['e', 'u'], 'xv': ['x'], 'xw': ['o', 'a'], 'xx': ['x'], 'xy':
['o', 'a', 'e'], 'xz': 0, 'ya': ['a', 'c', 'l', 'o', 'd',
'x', 'e', 'k', 'h', 'i', 'm', 't', 'r', 'n', 'p'], 'yb':
['a', 'c', 'l', 'o', 'z', 'd', 'p', 'e', 'g', 'h', 'k',
'r', 'n', 'u', 's'], 'yc': ['a', 'c', 'l', 'o', 'd', 'p',
'e', 'k', 'h', 'm', 't', 'r', 'n', 's'], 'yd': ['a', 'l',
'o', 'z', 'e', 'k', 'h', 'm', 't', 'r'], 'ye': 1, 'yf': ['a',
'l', 'o', 'd', 's'], 'yg': ['a', 'c', 's', 'l', 'z', 'x',
'd', 'b', 'h', 'm', 'p'], 'yh': ['a', 'c', 'l', 'o', 'e',
'b', 't', 'v', 'n', 'p'], 'yi': ['a', 'z', 'd', 'x', 'e',
'h', 'k', 'r', 'c', 'l', 't', 'v', 'n', 'g', 'b', 'm',
'p', 'f', 'o', 'u', 's'], 'yj': ['k'], 'yk': ['d', 't'], 'yl':
['a', 'c', 's', 'l', 'o', 'z', 'd', 'x', 'g', 'e', 'h',
'b', 'k', 'm', 't', 'r', 'n', 'p'], 'ym': ['a', 'c', 'l',
'o', 'z', 'x', 'd', 'g', 'e', 'h', 't', 'r', 'n', 's'],
'yn': ['a', 'c', 'l', 'o', 'd', 'e', 'g', 'h', 'm', 'r',
's'], 'yo': ['a', 'c', 'l', 'o', 'e', 'h', 'b', 'm', 'r',
'n', 'u', 'p'], 'yp': ['a', 'c', 'l', 'o', 'g', 'e', 'h',
'b', 't', 'r', 'n', 's'], 'yq': 0, 'yr': ['a', 's', 'l', 'o',
'g', 'b', 'h', 'k', 'm', 't', 'p'], 'ys': ['a', 'c', 'l',
'o', 'd', 'x', 'e', 'h', 'b', 'k', 'v', 'm', 't', 'r',
'n', 'u', 's'], 'yt': ['a', 'c', 's', 'l', 'd', 'h', 'b',
'm', 't', 'r', 'n', 'p'], 'yu': ['a', 'l'], 'yv': ['g', 'l'],
'yw': ['a', 'c', 'l', 'd', 'p', 'e', 'g', 'b', 'k', 'v',
't', 'r', 'n', 's'], 'yx': ['c', 'l', 'h', 'm', 'n', 'p'],
'yy': 0, 'yz': ['l', 'b'], 'za': ['a', 'c', 'y', 'z', 'g', 'e',
'i', 'n', 'u'], 'zb': ['z'], 'zc': 0, 'zd': ['i'], 'ze': 1, 'zf': 0,
'zg': 0, 'zh': 0, 'zi': ['a', 'y', 'w', 'o', 'z', 'e', 'i',
't', 'r', 'n', 'u'], 'zj': 0, 'zk': ['t'], 'zl': ['o', 'z'],
'zm': ['i', 'z'], 'zn': 0, 'zo': ['a', 'o', 'z', 'e', 'i', 't',
'r', 'n', 'u'], 'zp': ['a', 't'], 'zq': 0, 'zr': 0, 'zs': 0, 'zt': 0,
'zu': ['a', 'i', 'd'], 'zv': ['t', 'e'], 'zw': ['z'], 'zx': 0,
'zy': ['a', 'w', 'o', 'z', 'e', 't', 'n', 'u'], 'zz': ['a',
'o', 'e', 'i', 'u']}

string = ''
with open(sys.argv[1]) as file:
    for line in file:
        string += line

def somdev(string, bigrams):
    i = bad = good = total = 0
    string = string.lower()
    previous_char = '*'
    string_length = len(string)
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    while i < string_length - 1:
        current_char = string[i]
        next_char = string[i + 1]
        if next_char not in alphas:
            next_char = '*'
            if previous_char == '*' and current_char in 'bcdefghjklmnopqrstuvwxyz':
                bad += 1
            previous_char = current_char
            i += 1
            continue
        if current_char in alphas:
            bigram = current_char + next_char
            value = bigrams[bigram]
            if value == 0:
                bad += 1
            elif value == 1:
                good += 1
            else:
                if previous_char in value or previous_char == '*':
                    good += 1
                else:
                    bad += 1
            total += 1
        previous_char = current_char
        i += 1
    return total, good, bad

time_start = time.time()

total, good, bad = somdev(string, bigrams)

time_end = time.time()

time_taken = time_end - time_start

print('\n---Result---')
print('- Text length: %i bytes'% len(string))
print('- English text length: %i bytes' % len(re.findall(r'[a-zA-Z]', string)))
print('- Total valid bigrams: %i' % total)
print('- Pronounceable bigrams: %i' % good)
print('- Unpronounceable bigrams: %i' % bad)
print('- Meaningful text: %i%%' % ((good * 100)/total))

print('\n---Benchmark---')
print('- Parsing started: %i' % time_start)
print('- Parsing ended: %i' % time_end)
print('- Time taken: %i seconds' % time_taken)
print('')
