from django.db import models


class Logic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    FUNCTION_CHOICES = (
        ('stringClean', 'stringClean'),
        ('maxBlock', 'maxBlock'),
        ('reorderBlock', 'reorderBlock'),
    )
    function = models.CharField(choices=FUNCTION_CHOICES,
                                blank=False,
                                max_length=25)
    input_string = models.TextField()
    result = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)

    def stringClean(self, input_string):
        l = list(input_string)
        i = 0
        while i < len(l) - 1:
            if l[i] == l[i+1]:
                l.pop(i)
            else:
                i += 1
        return ''.join(l)

    def maxBlock(self, input_string):
        mx = 0
        temp_mx = 0
        for i in range(len(input_string) - 1):
            if input_string[i] == input_string[i+1]:
                temp_mx += 1
                if temp_mx > mx:
                    mx = temp_mx
            else:
                temp_mx = 1
        return mx

    def reorderBlock(self, input_string):
        return ''.join(sorted(list(input_string)))

    def save(self, *args, **kwargs):
        """
        Deal with Logic Implementation 1
        """
        result = ''
        if self.function == 'stringClean':
            result = self.stringClean(self.input_string)
        if self.function == 'maxBlock':
            result = self.maxBlock(self.input_string)
        if self.function == 'reorderBlock':
            result = self.reorderBlock(self.input_string)
        self.result = result
        super(Logic, self).save(*args, **kwargs)
