from crewai import Flow, listen, start, route

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam 0 alikum")