from controller.models import Channel

source_list = []
channel_list = []

for item in Channel.objects.all():
    channel_list.append(item.__str__())
channel_quantity = len(channel_list)
for el in Channel.objects.all():
    source_list.append(el.get_source())
# searching number of pages
if channel_quantity%10 == 0:
    max_page = channel_quantity/10
else:
    max_page = int(channel_quantity/10+1)



