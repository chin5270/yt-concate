from steps.get_all_video import GetVideoList
from steps.step import StepException
CHANNEL_ID = 'UCudk4X86eRN6H2psDpP2LFg'
steps = [
    GetVideoList(),
]

for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception happened:',e)
        break