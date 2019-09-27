import logging
import demoPack.drawings.myModule as myModule

# create logger with 'training_demo_application'
logger = logging.getLogger('training_demo_application')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('training_demo.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of demoPack.drawings.myModule.Box')
b1 = myModule.Box(10, 3, 5)
logger.info('created an instance of demoPack.drawings.myModule.Box')
logger.info('calling demoPack.drawings.myModule.Box.getVolume()')
v = b1.getVolume()
logger.info('finished demoPack.drawings.myModule.Box.getVolume()')
logger.info('calling demoPack.drawings.myModule.Box.displayBox()')
b1.displayBox()
logger.info('done with demoPack.drawings.myModule.Box.displayBox()')
