from django import forms


class Kydolex_PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    title_sub = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)


class Kydolex_PostForm2(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    sub = forms.CharField(max_length=30, label='タイトル')
    sub_content = forms.CharField(max_length=30, label='中間')
    sub_content2 = forms.CharField(max_length=30, label='中間')
    sub_content3 = forms.CharField(max_length=30, label='中間')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    sub_content = forms.CharField(label='中間本文', widget=forms.Textarea())
    sub_content2 = forms.CharField(label='中間本文', widget=forms.Textarea())
    sub_content3 = forms.CharField(label='中間本文', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)
    sub_image = forms.ImageField(label='イメージ画像', required=False)
    sub_image2 = forms.ImageField(label='イメージ画像', required=False)
    sub_image3 = forms.ImageField(label='イメージ画像', required=False)


class Kydolex_PostForm3(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    title_name = forms.CharField(max_length=30, label='name')
    title_id = forms.CharField(max_length=30, label='id')
    title_url = forms.CharField(max_length=30, label='url')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)


class Kydolex_PostForm4(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False)


class Kydolex_PostForm5(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)

class Kydolex_list_WebDesign_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())

class Kydolex_list_UIUX_Form(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())

class Kydolex_list_Icon(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())

class Kydolex_list_3D(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())


class Kydolex_list_graphic(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())


class Kydolex_list_video(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())


class Kydolex_list_Photograth(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())


class Kydolex_list_Image(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())


class Kydolex_list_Blog(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    image = forms.ImageField(label='イメージ画像', required=False)
    content = forms.CharField(label='説明', widget=forms.Textarea())
    content_url = forms.CharField(label='URL', widget=forms.Textarea())

