<template>
  <div class="common-layout">
    <el-container>
      <el-header class="centered-text">辽宁工程技术大学退役复学系统</el-header>
      <el-container>
        <!-- <div > -->
          <el-aside class="yellow-background" width ="125px"  >
            <a-menu :default-selected-keys="['1']" mode="inline" style="height:100%" >
              <a-menu-item key="1" icon="user" >
                <router-link to="/Table">学生信息</router-link>
              </a-menu-item>
            </a-menu>
        </el-aside>
        <!-- </div> -->
        <el-main>
          <RouterView></RouterView>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import { reactive, ref, watch, VueElement, h } from 'vue';
import { MailOutlined, AppstoreOutlined, SettingOutlined } from '@ant-design/icons-vue';
import type { MenuProps, ItemType } from 'ant-design-vue';

const selectedKeys = ref<string[]>(['1']);
const openKeys = ref<string[]>(['sub1']);

function getItem(
  label: VueElement | string,
  key: string,
  icon?: any,
  children?: ItemType[],
  type?: 'group',
): ItemType {
  return {
    key,
    icon,
    children,
    label,
    type,
  } as ItemType;
}

const items: ItemType[] = reactive([
  getItem('Navigation One', 'sub1', () => h(MailOutlined), [
    getItem('Item 1', 'g1', null, [getItem('Option 1', '1'), getItem('Option 2', '2')], 'group'),
    getItem('Item 2', 'g2', null, [getItem('Option 3', '3'), getItem('Option 4', '4')], 'group'),
  ]),


  
]);

const handleClick: MenuProps['onClick'] = e => {
  console.log('click', e);
};

watch(openKeys, val => {
  console.log('openKeys', val);
});
</script>
<style>
  .centered-text {
    text-align: center; /* 水平居中 */
    /* line-height: 100px; 垂直居中 */
    font-size: 25px; /* 字体大小为 100px */
    background-color: lemonchiffon; /* 设置背景颜色为柠檬黄 */
    padding-top: 15px; /* 设置内部内容与上边框的距离为5px */
  }
  .yellow-background {
    background-color: lemonchiffon; /* 设置背景颜色为柠檬黄 */
    width:"200px"
  }
</style>

