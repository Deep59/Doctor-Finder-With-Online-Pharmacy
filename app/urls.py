from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Indexpage,name="index"),
    path("contact/",views.ContactPage,name="contact"),
    path("aboutus/",views.AboutusPage,name="aboutus"),
    path("termscondtions/",views.TermsAndConditionsPage,name="termscondtions"),
    path("privacy/",views.Privacy_Policy,name="privacy"),

    # ======= Functionality urls ========= # 

    #Doctor AND Patient
    path("login",views.Loginuser,name="login"),
    path("insert",views.InsertData,name="insert"),
    path("doctorregisterpage/",views.DoctorRegisterPage,name="doctorregisterpage"),
    path("paitentregistepage/",views.PaitentRegisterPage,name="paitentregistepage"),
    path("pharmaregisterpage/",views.PharmacyRegisterPage,name="pharmaregisterpage"),
    path("doctorlogin/",views.DoctorLoginpage,name="doctorlogin"),
    path("patientlogin/",views.PatientLoginpage,name="patientlogin"),
    path("pharmacylogin/",views.PharmacyLoginpage,name="pharmacylogin"),
    path("verifyotp/",views.VerifyOtp,name="verifyotp"),
    path("forgotpass/",views.ForgotPassword,name="forgotpass"),
    path("enteremail/",views.Enter_Mail,name="enteremail"),
    path("verifyotpforgotpass/",views.VerifyOtpForgotPassword,name="verifyotpforgotpass"),
    path("userforgotpass/",views.Forget_Password,name="userforgotpass"),
    path("forgotpass/",views.ForgotPassword,name="forgotpass"),
    path("dchangepass/",views.Doc_Change_Password,name="dchangepass"),
    path("docchangepass/",views.Doctor_Change_Password,name="docchangepass"),
    path("pchangepass/",views.Pat_Change_Password,name="pchangepass"),
    path("patchangepass/",views.Patient_Change_Password,name="patchangepass"),
    path("pdashboard/",views.PatientDash,name="pdashboard"),
    path("ddashboard/",views.DoctorDash,name="ddashboard"),
    path("phadash/",views.PharmacyDash,name="phadash"),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("updatedoc/<int:pk>",views.UpdateDocData,name="updatedoc"),
    path("updatepat/<int:pk>",views.UpdatePatData,name="updatepat"),
    path("updatepha/<int:pk>",views.UpdatePhaData,name="updatepha"),
    path("logout<int:pk>/",views.Logout,name="logout"),
    path("showalldoctor/",views.ShowAllDoctor,name="showalldoctor"),
    path("doctordetail",views.DoctorDetails,name="doctordetail"),
    path("doctordescription/<int:pk>",views.DoctorDecription,name="doctordescription"),
    path("schedule/",views.SchedulePage,name="schedule"),

    #Appointment
    path("insertavail/<int:pk>",views.AvailabilityInsert,name="insertavail"),
    path("appointmentpage/",views.BookAppointmentPage,name="appointmentpage"),
    path("acceptappintment/<int:pk>",views.AcceptAppintDoc,name="acceptappintment"),
    path("fetchdatabyid/<int:pk>",views.FetchByIdData,name="appointmentp"),
    path("insertappointment<int:pk>",views.InsertAppintment,name="insertappointment"),
    path("confirmPage/",views.ConfirmPay,name="confirmPage"),
    path("confirm/",views.ConfirmAndPay,name="confirm"),
    path("checkoutpage/",views.CheckOut,name="checkoutpage"),
    path("savebooking/",views.SaveBookingSummary,name="savebooking"),
    path("showallappo/",views.ShowAllPatientAppointment,name="showallappo"),
    path("showappo/",views.ShowAppointmentpatient,name="showappo"),

    #Case
    path("Casepage/",views.Casepage,name="Casepage"),
    #path("fetchdatabyidcase/<int:pk>",views.FetchByIdDataCase,name="fetchdatabyidcase"),
    path("insertcase/<int:pk>",views.InsertCase,name="insertcase"),
    path("showcase/",views.ShowPatientCase,name="showcase"),

    # path("response/<int:pk>/<str:resp>/",views.appointment_resp,name="response"),

    #Prescription
    path("prescription/",views.prescription,name="prescription"),

    #Admin
    path("Admin/",views.Adminpage,name="Admin"),
    path("adminlogin/",views.AdminLoginPage,name="adminlogin"),
    path("adlogin/",views.AdminLogin,name="adlogin"),
    path("adlogout/",views.AdminLogout,name="adlogout"),
    path("doctable/",views.AdminDocUserTablePage,name="doctable"),
    path("phatable/",views.AdminPhaUserTablePage,name="phatable"),
    path("admindocprofilepage/<int:pk>",views.AdminDocProfilePage,name="admindocprofilepage"),
    path("addocprofile/<int:pk>",views.AdminDocUpadatePage,name="addocprofile"),
    #path("adminpatprofilepage/<int:pk>",views.AdminPatProfilePage,name="adminpatprofilepage"),
    #path("adpatprofile/<int:pk>",views.AdminDocPatUpadatePage,name="adpatprofile"),
    

    #Pharmacy 
    path("category/",views.category,name="category"),
    
    path("Category/",views.Addcategory,name="Category"),
    path("showcategory/",views.showcategory,name="showcategory"),
    path("Addproduct/",views.product,name="Addproduct"),
    path("AddProduct/<int:pk>",views.AddProduct,name="AddProduct"),
    path("Showproduct/<int:pk>",views.Showallproduct,name="Showproduct"),
    path("updatepro/<int:pk>",views.UpdateProduct,name="updatepro"),
    path("Updateproduct/<int:pk>",views.Uppro,name="Updateproduct"),
    path("deleteProduct/<int:pk>",views.DeleteProduct,name="deleteProduct"),

    #Customer
    path("showproductcust/",views.ShowProduct,name="showproductcust"),
    path("homepharmacy/",views.Homepharmacy,name="homepharmacy"),
    path("productdes/<int:pk>",views.productdes,name="productdes"),
    path("addcart/<int:pk>",views.Addtocart,name="addcart"),
    path("cartpro/<int:pk>",views.CartProduct,name="cartpro"),
    path("deletecartPro/<int:pk>",views.DeletecartProduct,name="deletecartPro"),
    path("search/",views.search,name="search"),
    path("Homepharmacycat/",views.Homepharmacycat,name="Homepharmacycat"),
    path("checkout/<int:pk>",views.Proceedtocheckout,name="checkout"),
    path("checkout1/<int:pk>",views.checkout,name="checkout1"),
]