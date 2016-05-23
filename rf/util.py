import collections


class IterMultipleComponents(object):

    def __init__(self, stream, key=None, number_components=None):
        substreams = collections.defaultdict(stream.__class__)
        for tr in stream:
            k = (tr.id[:-1], str(tr.stats[key]) if key is not None else None)
            substreams[k].append(tr)
        n = number_components
        self.substreams = [s for _, s in sorted(substreams.items())
                           if n is None or len(s) == n or len(s) in n]

    def __len__(self):
        return len(self.substreams)

    def __iter__(self):
        for s in self.substreams:
            yield s


def direct_geodetic(lonlat, azi, dist):
    from geographiclib.geodesic import Geodesic
    coords = Geodesic.WGS84.Direct(lonlat[1], lonlat[0], azi, dist*1000)
    return coords['lon2'], coords['lat2']
