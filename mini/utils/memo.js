const app = getApp()

function memoDict(callback){
  wx.request({
    url: app.globalData.host + '/memo/get_user_memo_dict',
    method: 'POST',
    data: {
      open_id: openid
    },
    success(res) {
      console.log(res)
      app.globalData.memo_dict = JSON.stringify(res.data.dict)
      
      p.setData({
        memo_dict: JSON.parse(app.globalData.memo_dict),
        length: JSON.parse(app.globalData.memo_dict).length
      })
    }
  })

}

//获取用户的生词字典
function getMemoDict(openid,p) {
  let promise = new Promise((resolve,reject)=>{
    wx.request({
      url: app.globalData.host + '/memo/get_user_memo_dict',
      method: 'POST',
      data: {
        open_id: openid
      },
      success(res) {
        console.log(res)
        app.globalData.memo_dict = JSON.stringify(res.data.dict)

        p.setData({
          memo_dict: JSON.parse(app.globalData.memo_dict),
          length: JSON.parse(app.globalData.memo_dict).length
        })
        resolve(res)
      }
    })
    })
  return promise
  }
  


module.exports.getMemoDict = getMemoDict