
class traverse(object):

# given a point, find all the routes to get to the end of the line, looking for points
    def traverse_journey(self, point, path_routes=[]): # start by passing in path_routes = []

        if (point is not None):
            path = point.get_active_path()
            print('> active path found. First route on active path is ', point.route_paths[0][0].get_route_name())
            for route in path:
                print('anoter route found ', route.get_route_name())
                path_routes.append(route)
                if route.point:
                    print('Current active path has another point at route: ', route.get_route_name())
                    self.traverse_journey(route.point, path_routes)
                    return path_routes

        print('finished traversing')
        for i, n in enumerate(path_routes):
            print(i, ' route name ', n.get_route_name())
        return path_routes 
