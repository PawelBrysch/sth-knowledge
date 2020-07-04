from scipy.stats import rv_continuous

def RandomObservationGenerator(custom_pdf, min_, max_):
    class CustomRV2(rv_continuous):
        def __init__(self, *args, **kwargs):
            rv_continuous.__init__(self, *args, **kwargs)
            self.custom_pdf = custom_pdf

        def _pdf(self, x):
            return self.custom_pdf(x)
    rv_object = CustomRV2(a=min_, b=max_)
    while True:
        yield rv_object.rvs()