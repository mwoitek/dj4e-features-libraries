from ads.models import Ad
from ads.owner import OwnerCreateView
from ads.owner import OwnerDeleteView
from ads.owner import OwnerDetailView
from ads.owner import OwnerListView
from ads.owner import OwnerUpdateView


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad
