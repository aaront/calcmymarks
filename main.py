#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    main.py
    ~~~~~~~

    Implements the request handlers for CalcMyMarks

    :copyright: (c) 2009-2010 by Aaron Toth.
    :license: Apache 2.0, see LICENSE for more details.
"""



from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from markcalc import MarkCalc

import os
import cgi

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), os.path.join("templates", 'index.html'))
        self.response.out.write(template.render(path, template_values))
        
class ErrorHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), os.path.join("templates", 'error.html'))
        self.response.out.write(template.render(path, {}))
    
class Calculate(webapp.RequestHandler):
    def get(self):
        self.redirect("/error")
    
    def post(self):
        try:
            orig = float(self.request.get('orig'))
        except:
            self.redirect("/error")
            
        curr = self.request.get_all('curr')
        eval = self.request.get_all('eval')
        tally = self.request.get_all('tally')
        choice = self.request.get('type')
        
        current = []
        for i in range(len(curr)):
            try:
                curr[i] = float(curr[i])
                eval[i] = cgi.escape(str(eval[i]))
                tally[i] = float(tally[i])
                current.append([curr[i], eval[i], tally[i]])
            except:
                self.redirect("/error")
        
        mk = MarkCalc(current)
        
        if (choice == 'course'):
            result = mk.needed(orig)
            result_str = ["You need a", "on the final exam to get a %0.1f%% in the course" % orig]
        else:
            result = mk.whatif(orig)
            result_str = ["If you get a %0.1f%% on the final exam, you'll get a" % orig, "in the course"]
        
        tally.append(mk.exam_total())
        eval.append("Exam")
        
        template_values = {
            'curr': curr,
            'eval': eval,
            'tally': tally,
            'len_curr': len(curr),
            'result': round(result, 2),
            'result_str': result_str,
        }
        
        path = os.path.join(os.path.dirname(__file__), os.path.join("templates", 'result.html'))
        self.response.out.write(template.render(path, template_values))
    
def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/result', Calculate),
                                        ('/error', ErrorHandler)],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
