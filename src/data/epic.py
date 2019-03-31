class Epic():
    def __init__(self):
        self.project_id = None  # int
        self.name = None  # string
        self.label = None  # string
        self.label_id = None  # int
        self.description = None  # string
        self.comments = None  # List[comment]
        self.pull_requests = None  # List
        self.branches = None  # List[branch]
        self.followers = None  # List[follower]
        self.follower_id = None  # List[int]
        self.after_id = None  # int
        self.before_id = None  # int

    def get_body(self):
        body = "{"
        if self.name != None:
            body = body + "\"name\":\"" + self.name + "\","
        if self.label != None:
            body = body + "\"label\":\"" + self.label + "\","
        if self.label_id != None:
            body = body + "\"label_id\":\"" + str(self.label_id) + "\","
        if self.description != None:
            body = body + "\"description\":\"" + self.description + "\","
        if self.comments != None:
            body = body + "\"comments\":\"" + str(self.comments) + "\","
        if self.pull_requests != None:
            body = body + "\"pull_requests\":\"" + str(self.pull_requests) + "\","
        if self.branches != None:
            body = body + "\"branches\":\"" + str(self.branches) + "\","
        if self.followers != None:
            body = body + "\"followers\":\"" + str(self.followers) + "\","
        if self.follower_id != None:
            body = body + "\"follower_id\":\"" + str(self.follower_id) + "\","
        if self.after_id != None:
            body = body + "\"after_id\":\"" + str(self.after_id) + "\","
        if self.before_id != None:
            body = body + "\"before_id\":\"" + str(self.before_id) + "\","
        if body[len(body -1)] == ",":
            body[len(body - 1)] = ""
        body = body + "}"
        print "body: " + body
        return body
