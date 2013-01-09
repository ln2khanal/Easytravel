'''
Created on Dec 15, 2012

@author: mama
'''
# import flask, flask.views
from flask import jsonify
from getgraph import getdata
from getroute import shortestpath

def compute(node_a, node_b):
        node_graph = getdata()
        message = None
        if ((node_a == "" or node_a == None) or (node_a == "" or node_a == None)):            
            message = jsonify(status="failed", message="Please provide the station name properly.")
            return  message
        if (node_a == node_b):
            if(node_a not in node_graph):
                message = jsonify(status="failed", message="Unknown source and destination stations.")
            else:
                message = jsonify(status="success", route="Please alter the source and destination stations.", distance="0")
            return  message

        if  ((node_a in node_graph) and (node_b in node_graph)):
            report = shortestpath(node_graph, node_a, node_b, [], {}, {})
        
            route = ""
            for i in range(0,len(report[1])):
                route +=report[1][i]+""
            message = jsonify(status="success", route=route, distance=report[0])

            return  message
        else:
            message = jsonify(status="failed", message="One or both of the station names are not found in the entire route.")
            return message
