import Ember from 'ember';

export default Ember.Controller.extend({
  carriers: ["UPS", "USPS", "FedEx", "DHL US", "DHL Global", "OnTrac", "ICC World", "LaserShip", "Canada Post"],
  selectedCarrier: null,
  trackingNum: null,

  actions: {
    submit: function() {
      if (this.get('selectedCarrier') == "UPS"){
        window.location.replace("http://wwwapps.ups.com/WebTracking/track?track=yes&trackNums=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "FedEx"){
        window.location.replace("http://www.fedex.com/Tracking?action=track&tracknumbers=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "USPS"){
        window.location.replace("https://tools.usps.com/go/TrackConfirmAction_input?qtc_tLabels1=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "DHL US"){
        window.location.replace("http://track.dhl-usa.com/TrackByNbr.asp?ShipmentNumber=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "DHL Global"){
        window.location.replace("http://webtrack.dhlglobalmail.com/?mobile=&trackingnumber=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "OnTrac"){
        window.location.replace("http://www.ontrac.com/trackingdetail.asp?tracking=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "ICC World"){
        window.location.replace("http://iccworld.com/track.asp?txtawbno=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "LaserShip"){
        window.location.replace("http://www.lasership.com/track.php?track_number_input=" + `${this.get('trackingNum')}`);
      }
      else if (this.get('selectedCarrier') == "Canada Post"){
        window.location.replace("http://www.canadapost.ca/cpotools/apps/track/personal/findByTrackNumber?trackingNumber=" + `${this.get('trackingNum')}` + "&LOCALE=en");
      }
    }
  }
});
