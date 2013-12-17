 from planet.management.commands import planet_update_all_feeds

 @app.task(bind = True)
def load_feed_task(self):
  planet_update_all_feeds.Command().handle() 
