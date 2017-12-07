<style type="text/css">
 .billing_address {
    background: #ebebeb;
    padding: 10px;
    border-radius: 5px;
    line-height: 22px;
    float: left;
    margin-bottom: 20px;
    font-size: 18px;
    min-width: 30%;
    position: relative;
    color: #4e4e4e;
}
  .billing_address span.name{
    font-weight: bold;
    margin-bottom: 5px;
    display: inline-block;
  }
  span.edit_icon {
    position: absolute;
    right: 10px;
    font-size: 24px;
    bottom: 10px;
    z-index: 99;
}
/*----------------------*/
.np_login_input_content{margin:0;}
.signup_custom .np_login_input_content {
    width: 100%;
}
.dis_table {
    display: table;
    width: 100%;
}
.dis_row {
    display: table-row;
}
.dis_cell {
    display: table-cell;
    vertical-align: top;
}
.fields_Dv_prof {
    clear: both;
    float: left;
    margin-bottom: 15px;
    text-align: left;
    width: 100%;
}
.fields_Dv_prof input[type="text"], .fields_Dv_prof input[type="password"], .signup_form .col-md-12 .col-md-6 div input[type="text"] {
    border: 1px solid #bdc3c7;
    box-sizing: border-box;
    box-shadow: 3px 3px 2px #333;
    font-size: 14px;
    margin-bottom: 0;
    padding: 5px;
    width: 100%;
}
.signup_custom .np_login_input_content .np_login_inputbox:first-child {
  padding-right: 10px !important;
}
.np_login_inputbox .text_filelds, .np_login_chk_val {
  border: 2px solid #bdc3c7;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  width: 100%;
  box-shadow: none;
  color: #4E4E4E;
  font-family: "Lato",Helvetica,Arial,sans-serif;
  font-size: 15px;
  height: 42px;
  line-height: 1.467;
  padding: 0px 12px;
  transition: border 0.25s linear 0s, color 0.25s linear 0s, background-color 0.25s linear 0s;
}
.np_login_inputbox {
  float: left;
  width: 100%;
  height: 46px;
}
.fst_box.fst_box2 {
  width: 50%;
}
.pad_20_40 {
  background: #ebebeb none repeat scroll 0 0;
  border-radius: 10px;
  margin: 14px;
  padding: 10px 30px;
}
.label_Dv_prof {
  font-weight: bold;
  height: 26px;
  line-height: 25px;
  text-align: left;
  width: 100%;
  font-size: 14px;
}
.btm_box > div {
  background: #eeeeee none repeat scroll 0 0;
  border-radius: 5px;
  min-height: 225px;
  padding: 20px;
}
.checkbox.checked .second-icon, .radio.checked .second-icon, .btm_box h1, .btm_box span, .btm_box a {
  color: #35589A;
}
.np_login_input_content .btn_go {
  margin-left: 0px;
  background-color: #0C76BC;
  border: medium none;
  border-radius: 0;
  color: #fff;
  padding: 5px 24px;
}
.np_login_input_content .btn_go, button.btn_go {
  background: #35589A;
  color: #ffffff;
}
.sub_text {
  background: #35589A;
  border-radius: 50%;
  color: #fff;
  padding: 1px 6px;
  margin-left: 5px;
}
.sub_text.pos_relative > a {
  color: #fff;

}
.np_signup_button_stripe, .np_signup_button_new {
  padding: 10px 15px !important;
  border-radius: 4px !important;
}
.signup_custom .np_login_input_content .np_login_inputbox:nth-child(2) {
  padding-left: 10px !important;
}
.np_login_input_content {
  float: left;
  width: 100%;
  margin-top: 13px;
}
*::-moz-placeholder{color:#4e4e4e !important;}
.sum_tbl{
  border-left: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  float: right;
}
.sum_tbl td{
  padding: 7px;
  border-top: 1px solid #ccc;
  border-right: 1px solid #ccc;
  }
.agreeTxt{
  /*font-size: 10px;*/
  color:#555;
}
.dis_table{
  color:#555;
}
.edit_icon a:hover{
  text-decoration: none;
}
.billing_data
{
    margin-bottom: 10px;
}
</style>
<div class="col-lg-12 padding-null">
    <form id="subscription_form">
  <div class="pull-left camp_hd">Upgrade</div>
<div id="wrapper">
  <div class="h_space10"></div>
  <div id="page-wrapper" class="pddng_rl_15">
    <div class="page-content">
      <div class="clearfix h_space10"></div>
      <div class="col-lg-12 padding-null">
        <div class="container-fluid">
          <div class="billing_address">
            <span class="name"><?=$vr_user->cname?></span><br>
            <?=$vr_user->address?> <br/>
            <?=$vr_user->company_city?> <br>
            <?=$vr_user->company_state.' '.$vr_user->company_zip?><br>
            <a href="#"><?=$vr_user->uemail?> </a><br>
            <?=$vr_user->phone?> 
            <span class="edit_icon">
              <a href="#" data-toggle="modal" data-target="#flexModalAdd"><i class="icon-pencil2"></i></a>
            </span>
          </div>
<div class="clearfix"></div>
          <div class="col-md-8 mob" style="padding:0; margin-left:0; margin-right:0;">
                  <div class="pad_20_40 card-number" style="margin-right: 0px; margin-left: 0px;">
                <div class="dis_table">
                <div class="dis_row">
                  <div style="width: 30%;" class="dis_cell">
                    <div class="fields_Dv_prof ccdetails">
                      <div class="label_Dv_prof">Name </div>
                
                      <div style="width: 98%;" class="field_Dv_prof pos_relative">
                        <input maxlength="16" id="name_on_card" class="form_field_text focusremove null_validate" name="name_on_card" value="" type="text">
                      </div>
                    </div>
                  </div>
                  <div style="width: 30%;" class="dis_cell">
                    <div class="fields_Dv_prof ccdetails">
                      <div class="label_Dv_prof">Card Number <span class="cardtype" style="display:none"></span></div>
                
                      <div style="width: 98%;" class="field_Dv_prof pos_relative">
                        <input maxlength="16" id="ccnumber" class="form_field_text  cc-number focusremove null_validate" name="ccnumber" value="" type="text">
                        <div class="credit_img"></div>
                      </div>
                    </div>
                  </div>
                  <div style="width: 10%;" class="dis_cell">
                    <div class="fields_Dv_prof ccdetails">
                      <div class="label_Dv_prof">Expiration Date</div>
                      <div style="width: 95%;" class="field_Dv_prof">
                        <input name="expire_date" style="display: none;" type="text">
                        <input maxlength="7" autocomplete="off" placeholder="MM/YY" class="cc-exp null_validate" id="cc-exp" name="expire_date" value="" type="text">
                      </div>
                    </div>
                    </div>
                    <div style="width: 10%;" class="dis_cell">
                    <div class="fields_Dv_prof ccdetails">
                      <div class="label_Dv_prof">Security Code <span class="sub_text pos_relative"><a href="javascript:void(0);">?</a><div class="tool_tip" style="display: none;"><img src="images/cvv-icon.png" alt="The 3 digit number printed on the back of the card."></div></span></div>
                      <div class="field_Dv_prof"> 
                        <input name="secure_code" style="display: none;" type="password"> 
                        <input maxlength="3" autocomplete="off" id="secure_code" class="form_field_text cc-cvc focusremove null_validate"  name="secure_code" value="" type="password">                      
                      </div>
                    </div>
                  </div>
                  
                </div>
                </div>
                </div>
                 </div>
                        </div>
        </div>
      </div>
      <div>
        <div class="row">
          <table class="table table-striped table-bordered table-hover table-green" id="" >
            <thead>
              <tr role="row">
                <th class=""  rowspan="1" colspan="1" style="width: 75%">Purchase</th>
                <th class=""  rowspan="1" colspan="1" >Quantity</th>
                <th class=""  rowspan="1" colspan="1" >Price</th>
                <th class=""  rowspan="1" colspan="1" >Amount</th>
              </tr>
            </thead>
            <tbody>
                <?php if($is_subscribe == 0){ ?>
              <tr>
                <td>Dynamic Hire initial license - This is one time purchase </td>
                <td>1<!-- <input type="number" name="initial_qty" id="initial_qty" min="1" max="5"> --></td>
                <td align="right"><?=$currency_symbol.number_format($price, 2);?></td>
                <td align="right"><span><?=$currency_symbol.number_format($price, 2);?></span></td>
              </tr>
              <?php } ?>
              <tr>
              <td><?=$is_subscribe == 1? 'Staff user accounts':'Includes 1 X Staff user account'?></td>
                <td><input type="number" name="staff_qty" class="quantity" id="staff_qty" min="<?=$is_subscribe == 0?1:0; ?>" value="<?=$is_subscribe == 0?1:0; ?>"></td>
                <td align="right"><?=$currency_symbol.number_format($price_staff_credits, 2)?></td>
                <td align="right"><?=$currency_symbol?><span id="staff_qty_price">0.00</span></td>
              </tr>
              <tr>
                <td><?=$is_subscribe == 1? 'Video credits':'Includes 100 FREE Interview Credits'?></td>
                <td><input type="number" step="50" name="credits_qty" class="quantity" id="credits_qty" min="<?=$is_subscribe == 0?100:0; ?>" value="<?=$is_subscribe == 0?100:0; ?>"></td>
                <td align="right"><?=$currency_symbol.number_format($price_credits, 2)?></td>
                <td align="right"><?=$currency_symbol?><span id="credits_qty_price">0.00</span></td>
              
              </tr>
            </tbody>
          </table>
          <table cellpadding="0" cellspacing="0" border="0" class="sum_tbl table" style="width:200px;">
            <tr>
              <td><?=ucfirst(strtolower($price_tax_type))?></td><?php $actual_price = number_format($price); $tax = number_format(($actual_price*$price_tax_percent)/100,2);?>
              <td align="right" style="min-width: 120px;"><?=$currency_symbol?><span id="tax"><?=number_format($tax, 2)?></span></td>
            </tr>
            <tr>
              <td>Total</td>
              <td align="right"><?=$price_currency_profile[0].$price_currency_profile[1].$currency_symbol;?><span id="total_price"><?=number_format($tax+$actual_price, 2)?></span></td>
            </tr>
          </table>
          <div class="clearfix"></div>
          <div style="float: right; text-align: right;">
            <span class="agreeTxt"> <input type="checkbox" id="t_and_c" name="" value="1"> Agree Terms &amp; Conditions</span><br>
            <input type="submit" class="btn btn-lg btn-primary" name="Pay Now" value="Pay Now" />
          </div>
        </div>
       </div>
    </div>
    </div>
</form>
</div>
</div>
<div class="modal modal-flex fade" id="flexModalAdd" tabindex="-1" role="dialog" aria-labelledby="flexModalLabel" aria-hidden="true">
  <div class="modal-dialog tokenaddfrom">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title" id="flexModalLabel">Billing Address</h4>
      </div>
      <div class="modal-body">
        <div class="modal_frm_wrpr">
          <form class="wp_parent_form" id="billing_form" action="" method="" name="">
            <div class="modal_frm_wrpr_input">
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->cname?>" placeholder="Company name" name="cname" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->address?>" placeholder="Address" name="address" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->company_city?>" placeholder="City" name="company_city" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->company_state?>" placeholder="State" name="company_state" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->company_zip?>" placeholder="Zip" name="company_zip" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->uemail?>" placeholder="Email" name="uemail" id="" type="text">
              </div>
              <div class="modal_input_wrpr">
                <input class="form-control billing_data" value="<?=$vr_user->phone?>" placeholder="Mobile number" name="phone" id="" type="text">
              </div>

            </div>
            <div class="modal-footer">
              <button type="submit" class="btn-lg btn-primary">Save</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
<script type="text/javascript">
function validateForm() 
{
    var isValid = false;
    $('.null_validate').each(function() 
    {
        if ( ($(this).val()).trim() === '' )
        {
          $(this).addClass('error');
          isValid = true;
      }
      else
      {
          var field_name = this.name;
      var field_value = this.value;
      if((field_name=='fname' || field_name=='lname') && (stringValidation(field_value) == false))
      {
        isValid = true;
        $(this).addClass('error');
      }
      else if((field_name == 'phone') && (mobileValidation(field_value) == false))
      {
        isValid = true;
        $(this).addClass('error');
      }
      else if((field_name == 'email' || field_name == 're_email') && (emailValidation(field_value) == false))
      {
        isValid = true;
        $(this).addClass('error');
      }
      else if((field_name == 'ccnumber') && ($.isNumeric(field_value) == false || field_value.length != 16))
      {
        $(this).addClass('error');
      }
      else if((field_name == 'expire_date') && (expireDateValidation(field_value) == false))
      {
        isValid = true;
        $(this).addClass('error');
      }
      else if((field_name == 'secure_code') && (cvv_validation(field_value) == false))
      {
        isValid = true;
        $(this).addClass('error');
      }
      else
      {
        $(this).removeClass('error');
      }
      }
    });
    return isValid;
} 
$(".null_validate").on("blur", function()
{
  if ( ($(this).val()).trim() === '' )
  {
      $(this).addClass('error');
    }
  else
  {
    var field_name = this.name;
    var field_value = this.value;
    if((field_name=='fname' || field_name=='lname') && (stringValidation(field_value) == false))
    {
      $(this).addClass('error');
    }
    else if((field_name == 'phone') && (mobileValidation(field_value) == false))
    {
      $(this).addClass('error');
    }
    else if((field_name == 'email' || field_name == 're_email') && (emailValidation(field_value) == false))
    {
      $(this).addClass('error');
    }
    else if((field_name == 'ccnumber') && ($.isNumeric(field_value) == false || field_value.length != 16))
    {
      $(this).addClass('error');
    }
    else if((field_name == 'expire_date') && (expireDateValidation(field_value) == false))
    {
      $(this).addClass('error');
    }
    else if((field_name == 'secure_code') && (cvv_validation(field_value) == false))
    {
      $(this).addClass('error');
    }
    else
    {
      $(this).removeClass('error');
    }
    }
})
function stringValidation(str) 
{
    return /^[a-zA-Z()]+$/.test(str);
}
function mobileValidation(num)
{
  var regEx = /^[+-]?\d+$/;
  return regEx.test(num);
}
function emailValidation(emailAddress)
{
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(emailAddress);
}
function expireDateValidation(expire_date)
{
  var split = expire_date.split("/")
    var mm = +split[0]
    var yyyy = +split[1]

    if (isNaN(mm) || isNaN(yyyy)) 
      {return false;}

    if (mm < 1 || mm > 13) 
      {return false;}

    if (yyyy < 99) 
      yyyy += 2000;

    if (yyyy < 2016) 
      {return false;}

    var today = new Date();
    if (yyyy < today.getFullYear()) 
      return false;
    if (yyyy === today.getFullYear() && mm < today.getMonth() + 1) 
      return false;

    return true;
}
function cvv_validation(cvv)
{
  var myRe = /^[0-9]{3,4}$/;
    var myArray = myRe.exec(cvv);
    if(cvv!=myArray)
    {
      return false;
    }
    else
    {
        return true;  //valid cvv number
    }

}
var price_tax_percent = parseFloat("<?=$price_tax_percent?>");
var price_staff_credits = parseFloat("<?=$price_staff_credits?>");
var price_credits = parseFloat("<?=$price_credits?>");
var initial_price = parseFloat("<?=$price?>");
var is_subscribe = "<?=$is_subscribe?>";
$(document).ready(function()
{
    $(document).on("mouseleave", ".quantity", function()
    {
        var field_id = this.name+'_price';
        var quantity = parseFloat(this.value);
        var field = this.name;
        var new_price = 0;
        if(field == 'credits_qty')
        {
            if(quantity > 100)
            {
                if(is_subscribe != 1)
                    quantity = quantity-100;
                new_price = price_credits * quantity;
            }
            else if(quantity > 1 && is_subscribe == 1)
                new_price = price_credits * quantity;
            else
                new_price = 0;
        }
        else if(field == 'staff_qty')
        {
            if(quantity>1)
            {
                if(is_subscribe != 1)
                    quantity = quantity - 1;
                new_price = price_staff_credits * quantity;
            }
            else if(quantity == 1 && is_subscribe == 1)
                new_price = price_staff_credits * quantity;
            else
                new_price = 0;
        }
        $("#"+field_id).html(new_price.toFixed(2));
        var credits_qty_price = parseFloat($("#credits_qty_price").text());
        var staff_qty_qty_price = parseFloat($("#staff_qty_price").text());
        
        var new_tax = parseFloat(((credits_qty_price+staff_qty_qty_price+initial_price)*price_tax_percent)/100);
        new_tax = new_tax.toFixed(2);
        $("#tax").text(new_tax);
        console.log(credits_qty_price+"+"+staff_qty_qty_price+"+"+initial_price+"+"+new_tax);
        var total_price = (credits_qty_price+staff_qty_qty_price+initial_price+parseFloat(new_tax));
        total_price = parseFloat(total_price).toFixed(2);
        $("#total_price").text(total_price);
    });
  $("#subscription_form").on("submit", function(e)
  {
    e.preventDefault();
    if(is_subscribe == 1 && $("#staff_qty").val() < 1 && $("#credits_qty").val() < 50)
    {
        swal({
                title: "Required fields",
                text: "Please select quantity",
                type: "warning",
                closeOnConfirm: true
              });
        return false;
    }
    if(validateForm() == false)
    {
      if($("#t_and_c").is(':checked') == false)
      {
        swal({
                title: "Agree terms & conditions?",
                text: "Please check terms & conditions",
                type: "warning",
                closeOnConfirm: true
              });
        return false;
      }
      else
      {
        var form_data = $("#subscription_form").serialize();
        showgif(1);
        $.post("<?=base_url('upgrade')?>", form_data, function(data)
          {
            showgif(0);
            var data = JSON.parse(data);
            if(data.error == false)
            {
              swal({
                    title: "Success!",
                    text: data.message,
                    type: "success",
                    closeOnConfirm: true
                  },
                  function(isConfirm) 
                  {
                      if (isConfirm) 
                      {
                          window.location.href="<?=site_url('job-position')?>";
                      } 
                  });
            }
            else
            {
              swal({
                    title: "Error",
                    text: data.message,
                    type: "error",
                    closeOnConfirm: true
                  });
            }
          });
      }
    }
  });
    $("#billing_form").on("submit", function(e)
    {
        e.preventDefault();
        var billing_data = [];
        validate = true;
        jQuery(".billing_data").each(function()
        {
            if((this.value).trim() == '')
            {
                $(this).addClass('error');
                validate = false;
            }
            else
            {
                $(this).removeClass('error');
            }

            var obj = {};
            obj.name = this.name;
            obj.value = (this.value).trim();
            billing_data.push(obj);
        });
        if(validate == false)
        {
            return false;
        }
        $.post("<?=site_url('save-billing-address')?>", {billing_address:billing_data, billing_id: "<?=$vr_user->billing_id?>"}, function(data)
        {
            showgif(1);
            var data = JSON.parse(data);
            if(data.error == false)
            {
              swal({
                    title: "Success!",
                    text: data.message,
                    type: "success",
                    closeOnConfirm: true
                  },
                  function(isConfirm) 
                  {
                      if (isConfirm) 
                      {
                          window.location.reload();
                      } 
                  });
            }
            else
            {
              swal({
                    title: "Error",
                    text: data.message,
                    type: "error",
                    closeOnConfirm: true
                  });
            }
        });
    });
})
</script>