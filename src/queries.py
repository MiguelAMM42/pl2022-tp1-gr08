
def distByAddress(athletes):
    dist = {}
    for a in athletes:
        if a['modalidade'] in dist:
            dist[a['modalidade']].append(a)
        else:
            dist[a['modalidade']] = [a]

    return dist
