# Hands in Hand
*Infrared laser based ASL to Speech Converter using recycled tech*

# How to Run
- The application is lowkey kinda messy, but our `tensorflow` file is in the following directory (please use unix)
    - `best.pt`
- The application is built on top of Ultralytics YOLOv8 model, so please run inference using their [documentation](https://docs.ultralytics.com/modes/predict/)
- Their documentation is really weird

# Why?
Many of our members have audibly impared friends. It's almost impossible to communicate to people who don't understand ASL without some text (phone or paper), what if you didn't need text?

Our project uses a Lidar lens camera mixed with infrared to extract ASL hand gestures. It translates these gestures into text and projects the output to audio! Audibly impaired people no longer have to rely on some device to type out their message, instead they can simply sign in the way they are familiar with. The recipient of the message doesn't have to learn ASL since the audio projection will let them know what the person is saying. Therefore, both parties will have seamless comfortable communication without having to messily change modes of communication.

# How we built it
We fine tuned a image classification model (YOLOv8) using data we harvested at HackMIT ourselves. All the data is manually classified and fed into our model. After training, we were able to display the classified ASL and convert it to natural speech via an AI api (Deepgram). This extremely fast API allows us to have nearly instant feedback so the user can hear what the other person is signing.

## Challenges
Learning ASL is hard. Hacking an Xbox Kinect is hard. Manually sourcing, labelling and fine tuning a machine learning model is also hard 😂. But we somehow managed to overcome all of these thanks to our amazing hardworking teammates. We all pulled together our greatest strengths and were able to develop the MVP in time.

# Ect...
We're really proud of how we were able to quite literally hack an Xbox Kinect to provide us with high quality lidar and infrared camera outputs. We're also really proud of all the effort and manual hours we put into photographing and labeling training data for our model. It look a long time and was tedious, but it was worth it in the end.

We learned the importance of sample size and quantity of training data and how it related to epochs. We learned that despite having a modest training size, we still need to have multiple epochs (~50) to get serviceable results. Machine Learning and image classification is a time intensive task and needs plenty of preparation beforehand. We also learned that hardware is incredibly more difficult than software, and we're so happy to have an experience teammate guide us through it all.

## What's Next...
We want to size down the camera size (preferably something a user could wear) and significantly increase the training data size for the model. We also want to incorporate more words and motion based words into our alphabet corpus to increase the range of communication possible with this technology. At the moment it only supports "static" hand signs, aka ones that do not have too much movement.
