class Event:
    def __init__(self, event_date, event_name, start_hour, end_hour):

        if not (0 <= start_hour < 24) or not (0 <= end_hour < 24):
            raise ValueError("Start and end hours must be between 0 and 23.")
        if start_hour >= end_hour:
            raise ValueError("Start hour must be less than end hour.")
        
        self.event_name = event_name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.event_date = event_date


    def __str__(self):
        return f"Event: {self.event_name}\nDate: {self.event_date}\nStart Hour: {self.start_hour}\nEnd Hour: {self.end_hour}"
    
    @property
    def event_name(self):
        return self._event_name
    
    @event_name.setter
    def event_name(self, event_name):
        if not event_name.strip():
            raise ValueError("Event name can't be empty.")
        self._event_name = event_name


    @property
    def start_hour(self):
        return self._start_hour
    
    @start_hour.setter
    def start_hour(self, start_hour):
        if not 0 <= start_hour < 24:
            raise ValueError("Start Hour must be between 0 and 23.")
        self._start_hour =  start_hour


    @property
    def end_hour(self):
        return self._end_hour
    
    @end_hour.setter
    def end_hour(self, end_hour):
        if not 0 <= end_hour < 24:
            raise ValueError("End hour must be between 0 and 23.")
        self._end_hour = end_hour
        
    

    @property
    def event_date(self):
        return self._event_date
    
    @event_date.setter
    def event_date(self, event_date):
        self._event_date = event_date