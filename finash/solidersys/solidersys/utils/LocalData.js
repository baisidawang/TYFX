export function getLocalData(requestUrl, callback) {
  var localPath = requestUrl.moduleName + '_' + requestUrl.methodName;
  var data = require('../raws/' + localPath+'.js');
  callback(data.localData);
}


