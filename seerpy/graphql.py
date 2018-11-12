
def studyWithDataQueryString(studyId):
    return '''
        query {
            study (id: "%s") {
                id
                patient {
                    id
                }
                name
                channelGroups {
                    id
                    name
                    sampleRate
                    samplesPerRecord
                    recordLength
                    chunkPeriod
                    recordsPerChunk
                    sampleEncoding
                    compression
                    signalMin
                    signalMax
                    units
                    exponent
                    segments (fromTime: 1.0, toTime: 9000000000000) {
                        id
                        startTime
                        duration
                    }
                    channels {
                        id
                        name
                        channelType {
                            name
                            category
                        }
                    }
                }
            }
        }
    ''' % (studyId)


def dataChunksQueryString(studyId, channelGroupId, fromTime, toTime):
    return '''
        query {
            study (id: "%s") {
                id
                name
                channelGroup (channelGroupId: "%s") {
                    id
                    name
                    segments (fromTime: %f, toTime: %f) {
                        id
                        startTime
                        duration
                        dataChunks {
                            time
                            length
                            url
                        }
                    }
                }
            }
        }
    ''' % (studyId, channelGroupId, fromTime, toTime)
    
def getLabesQueryString(studyId, labelGroupId, fromTime, toTime, limit, offset):
        return '''
        query {
            study (id: "%s") {
                id
                name
                labelGroup (labelGroupId: "%s") {
                    id
                    name
                    labelType
                    description
                    labels (limit: %.0f, offset: %.0f) {
                        id
                        note
                        startTime
                        duration
                        timezone
                        tags {
                            id
                            tagType {
                                id
                                category {
                                        id
                                        name
                                        description
                                        }
                                value
                                }
                            }
                    }
                }
            }
        }
    ''' % (studyId, labelGroupId, limit, offset)


def labelGroupsQueryString(studyId):
        return '''
        query {
            study (id: "%s") {
                id
                name
                labelGroups {
                    id
                    name
                    labelType
                    description
                }
            }
        }
    ''' % (studyId)

def channelGroupsQueryString(studyId):
    return '''
        query {
            study(id: "%s") {
                id
                patient {
                    id
                }
                name
                channelGroups {
                    name
                    sampleRate
                    segments {
                        id
                    }
                }
            }
        }
    ''' % (studyId)

def studyListQueryString(searchTerm=''):
    return '''
        query {
            studies (searchTerm: "%s"){
                id
                patient {
                    id
                }
                name
            }
        }
    '''% (searchTerm)

def studyQueryStudy(studyId):
    return '''
        query {
            study(id: "%s") {
                id
                patient {
                    id
                }
                name
            }
        }
    ''' % (studyId)

def addLabelMutationString(groupId, startTime, duration, timezone):
    return '''
        mutation {
            addLabelsToLabelGroup(
                groupId: "%s",
                labels: [{ startTime: %f, duration: %f, timezone: %f }]
            ) {
                id
            }
        }
    ''' % (groupId, startTime, duration, timezone)

def addLabelsMutationString(groupId, labels):
    start = '''
        mutation {
            addLabelsToLabelGroup(
                groupId: "%s",
                labels: [''' % (groupId)
    end = ''']
                ) {
                id
            }
        }
        '''
    
    lst = ''
    for l in labels:
        lst = lst + '{ startTime: %f, duration: %f, timezone: %f },' % (l[0], l[1], l[2])
    
    return start + lst[:-1] + end

def addLabelGroupMutationString(studyId, name, description):
    return '''
        mutation {
            addLabelGroupToStudy(studyId: "%s", name: "%s", description: "%s") {
                id
            }
        }
    ''' % (studyId, name, description)

def removeLabelGroupMutationString(groupId):
    return '''
        mutation {
            removeLabelGroupFromStudy(groupId: "%s")
        }
    ''' % (groupId)
