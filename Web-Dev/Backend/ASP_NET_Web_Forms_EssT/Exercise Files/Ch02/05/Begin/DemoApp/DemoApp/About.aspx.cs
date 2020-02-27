using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace DemoApp
{
    public partial class About : Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            Title = "From code behind";
        }

        protected void btnSendInfo_Click(object sender, EventArgs e)
        {
            Title = "Button was clicked";
        }
    }
}