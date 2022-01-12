namespace DBDog
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.dgvDBStatus = new System.Windows.Forms.DataGridView();
            this.btnFresh = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.tabPage1 = new System.Windows.Forms.TabPage();
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.label1 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.lblMailFromName = new System.Windows.Forms.Label();
            this.lblAlarmInterval = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.lblFreshDataTableTime = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.lblAliveDeclareTime = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.lblMailAlarmTo = new System.Windows.Forms.Label();
            this.lblMailAliveTo = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.lblMailFrom = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.lblMailSmtp = new System.Windows.Forms.Label();
            this.dgvCfg = new System.Windows.Forms.DataGridView();
            this.tabPage3 = new System.Windows.Forms.TabPage();
            this.dgvCalc = new System.Windows.Forms.DataGridView();
            this.btnReadcfg = new System.Windows.Forms.Button();
            this.btnCalc = new System.Windows.Forms.Button();
            this.btnAliveDeclare = new System.Windows.Forms.Button();
            this.btnCheckThreshold = new System.Windows.Forms.Button();
            this.timerResetDeclareFlag = new System.Windows.Forms.Timer(this.components);
            this.timerRepeat = new System.Windows.Forms.Timer(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.dgvDBStatus)).BeginInit();
            this.tabControl1.SuspendLayout();
            this.tabPage1.SuspendLayout();
            this.tabPage2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCfg)).BeginInit();
            this.tabPage3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCalc)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvDBStatus
            // 
            this.dgvDBStatus.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvDBStatus.Location = new System.Drawing.Point(0, 6);
            this.dgvDBStatus.Name = "dgvDBStatus";
            this.dgvDBStatus.RowTemplate.Height = 23;
            this.dgvDBStatus.Size = new System.Drawing.Size(948, 380);
            this.dgvDBStatus.TabIndex = 0;
            // 
            // btnFresh
            // 
            this.btnFresh.Location = new System.Drawing.Point(13, 13);
            this.btnFresh.Name = "btnFresh";
            this.btnFresh.Size = new System.Drawing.Size(75, 23);
            this.btnFresh.TabIndex = 1;
            this.btnFresh.Text = "btnFresh";
            this.btnFresh.UseVisualStyleBackColor = true;
            this.btnFresh.Click += new System.EventHandler(this.btnFresh_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.tabPage1);
            this.tabControl1.Controls.Add(this.tabPage2);
            this.tabControl1.Controls.Add(this.tabPage3);
            this.tabControl1.Location = new System.Drawing.Point(13, 42);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(962, 418);
            this.tabControl1.TabIndex = 2;
            // 
            // tabPage1
            // 
            this.tabPage1.Controls.Add(this.dgvDBStatus);
            this.tabPage1.Location = new System.Drawing.Point(4, 22);
            this.tabPage1.Name = "tabPage1";
            this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage1.Size = new System.Drawing.Size(954, 392);
            this.tabPage1.TabIndex = 0;
            this.tabPage1.Text = "STATUS";
            this.tabPage1.UseVisualStyleBackColor = true;
            // 
            // tabPage2
            // 
            this.tabPage2.Controls.Add(this.label1);
            this.tabPage2.Controls.Add(this.label12);
            this.tabPage2.Controls.Add(this.lblMailFromName);
            this.tabPage2.Controls.Add(this.lblAlarmInterval);
            this.tabPage2.Controls.Add(this.label11);
            this.tabPage2.Controls.Add(this.lblFreshDataTableTime);
            this.tabPage2.Controls.Add(this.label10);
            this.tabPage2.Controls.Add(this.lblAliveDeclareTime);
            this.tabPage2.Controls.Add(this.label3);
            this.tabPage2.Controls.Add(this.label9);
            this.tabPage2.Controls.Add(this.lblMailAlarmTo);
            this.tabPage2.Controls.Add(this.lblMailAliveTo);
            this.tabPage2.Controls.Add(this.label8);
            this.tabPage2.Controls.Add(this.lblMailFrom);
            this.tabPage2.Controls.Add(this.label7);
            this.tabPage2.Controls.Add(this.lblMailSmtp);
            this.tabPage2.Controls.Add(this.dgvCfg);
            this.tabPage2.Location = new System.Drawing.Point(4, 22);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(954, 392);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "CFG";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(64, 5);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(83, 12);
            this.label1.TabIndex = 6;
            this.label1.Text = "mail_fromName";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(738, 41);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(89, 12);
            this.label12.TabIndex = 6;
            this.label12.Text = "ALARM_INTERVAL";
            // 
            // lblMailFromName
            // 
            this.lblMailFromName.AutoSize = true;
            this.lblMailFromName.Location = new System.Drawing.Point(155, 5);
            this.lblMailFromName.Name = "lblMailFromName";
            this.lblMailFromName.Size = new System.Drawing.Size(41, 12);
            this.lblMailFromName.TabIndex = 6;
            this.lblMailFromName.Text = "label6";
            // 
            // lblAlarmInterval
            // 
            this.lblAlarmInterval.AutoSize = true;
            this.lblAlarmInterval.Location = new System.Drawing.Point(833, 41);
            this.lblAlarmInterval.Name = "lblAlarmInterval";
            this.lblAlarmInterval.Size = new System.Drawing.Size(41, 12);
            this.lblAlarmInterval.TabIndex = 6;
            this.lblAlarmInterval.Text = "label6";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(714, 17);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(113, 12);
            this.label11.TabIndex = 5;
            this.label11.Text = "ALIVE_DECLARE_TIME";
            // 
            // lblFreshDataTableTime
            // 
            this.lblFreshDataTableTime.AutoSize = true;
            this.lblFreshDataTableTime.Location = new System.Drawing.Point(833, 29);
            this.lblFreshDataTableTime.Name = "lblFreshDataTableTime";
            this.lblFreshDataTableTime.Size = new System.Drawing.Size(41, 12);
            this.lblFreshDataTableTime.TabIndex = 5;
            this.lblFreshDataTableTime.Text = "label5";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(696, 29);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(131, 12);
            this.label10.TabIndex = 4;
            this.label10.Text = "FRESH_DATA_TABLE_TIME";
            // 
            // lblAliveDeclareTime
            // 
            this.lblAliveDeclareTime.AutoSize = true;
            this.lblAliveDeclareTime.Location = new System.Drawing.Point(833, 17);
            this.lblAliveDeclareTime.Name = "lblAliveDeclareTime";
            this.lblAliveDeclareTime.Size = new System.Drawing.Size(41, 12);
            this.lblAliveDeclareTime.TabIndex = 4;
            this.lblAliveDeclareTime.Text = "label4";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(72, 41);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(77, 12);
            this.label3.TabIndex = 3;
            this.label3.Text = "mail_alarmTo";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(750, 5);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(77, 12);
            this.label9.TabIndex = 3;
            this.label9.Text = "mail_aliveTo";
            // 
            // lblMailAlarmTo
            // 
            this.lblMailAlarmTo.AutoSize = true;
            this.lblMailAlarmTo.Location = new System.Drawing.Point(155, 41);
            this.lblMailAlarmTo.Name = "lblMailAlarmTo";
            this.lblMailAlarmTo.Size = new System.Drawing.Size(41, 12);
            this.lblMailAlarmTo.TabIndex = 3;
            this.lblMailAlarmTo.Text = "label3";
            // 
            // lblMailAliveTo
            // 
            this.lblMailAliveTo.AutoSize = true;
            this.lblMailAliveTo.Location = new System.Drawing.Point(833, 5);
            this.lblMailAliveTo.Name = "lblMailAliveTo";
            this.lblMailAliveTo.Size = new System.Drawing.Size(41, 12);
            this.lblMailAliveTo.TabIndex = 3;
            this.lblMailAliveTo.Text = "label3";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(90, 29);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(59, 12);
            this.label8.TabIndex = 2;
            this.label8.Text = "mail_from";
            // 
            // lblMailFrom
            // 
            this.lblMailFrom.AutoSize = true;
            this.lblMailFrom.Location = new System.Drawing.Point(155, 29);
            this.lblMailFrom.Name = "lblMailFrom";
            this.lblMailFrom.Size = new System.Drawing.Size(41, 12);
            this.lblMailFrom.TabIndex = 2;
            this.lblMailFrom.Text = "label2";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(90, 17);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(59, 12);
            this.label7.TabIndex = 1;
            this.label7.Text = "mail_smtp";
            // 
            // lblMailSmtp
            // 
            this.lblMailSmtp.AutoSize = true;
            this.lblMailSmtp.Location = new System.Drawing.Point(155, 17);
            this.lblMailSmtp.Name = "lblMailSmtp";
            this.lblMailSmtp.Size = new System.Drawing.Size(41, 12);
            this.lblMailSmtp.TabIndex = 1;
            this.lblMailSmtp.Text = "label1";
            // 
            // dgvCfg
            // 
            this.dgvCfg.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvCfg.Location = new System.Drawing.Point(6, 56);
            this.dgvCfg.Name = "dgvCfg";
            this.dgvCfg.RowTemplate.Height = 23;
            this.dgvCfg.Size = new System.Drawing.Size(942, 333);
            this.dgvCfg.TabIndex = 0;
            // 
            // tabPage3
            // 
            this.tabPage3.Controls.Add(this.dgvCalc);
            this.tabPage3.Location = new System.Drawing.Point(4, 22);
            this.tabPage3.Name = "tabPage3";
            this.tabPage3.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage3.Size = new System.Drawing.Size(954, 392);
            this.tabPage3.TabIndex = 2;
            this.tabPage3.Text = "CALC";
            this.tabPage3.UseVisualStyleBackColor = true;
            // 
            // dgvCalc
            // 
            this.dgvCalc.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvCalc.Location = new System.Drawing.Point(7, 6);
            this.dgvCalc.Name = "dgvCalc";
            this.dgvCalc.RowTemplate.Height = 23;
            this.dgvCalc.Size = new System.Drawing.Size(944, 380);
            this.dgvCalc.TabIndex = 0;
            // 
            // btnReadcfg
            // 
            this.btnReadcfg.Location = new System.Drawing.Point(95, 13);
            this.btnReadcfg.Name = "btnReadcfg";
            this.btnReadcfg.Size = new System.Drawing.Size(75, 23);
            this.btnReadcfg.TabIndex = 3;
            this.btnReadcfg.Text = "ReadCfg";
            this.btnReadcfg.UseVisualStyleBackColor = true;
            this.btnReadcfg.Click += new System.EventHandler(this.btnReadcfg_Click);
            // 
            // btnCalc
            // 
            this.btnCalc.Location = new System.Drawing.Point(176, 12);
            this.btnCalc.Name = "btnCalc";
            this.btnCalc.Size = new System.Drawing.Size(75, 23);
            this.btnCalc.TabIndex = 4;
            this.btnCalc.Text = "calc";
            this.btnCalc.UseVisualStyleBackColor = true;
            this.btnCalc.Click += new System.EventHandler(this.btnCalc_Click);
            // 
            // btnAliveDeclare
            // 
            this.btnAliveDeclare.Location = new System.Drawing.Point(258, 13);
            this.btnAliveDeclare.Name = "btnAliveDeclare";
            this.btnAliveDeclare.Size = new System.Drawing.Size(86, 23);
            this.btnAliveDeclare.TabIndex = 5;
            this.btnAliveDeclare.Text = "AliveDeclare";
            this.btnAliveDeclare.UseVisualStyleBackColor = true;
            this.btnAliveDeclare.Click += new System.EventHandler(this.btnAliveDeclare_Click);
            // 
            // btnCheckThreshold
            // 
            this.btnCheckThreshold.Location = new System.Drawing.Point(350, 13);
            this.btnCheckThreshold.Name = "btnCheckThreshold";
            this.btnCheckThreshold.Size = new System.Drawing.Size(75, 23);
            this.btnCheckThreshold.TabIndex = 6;
            this.btnCheckThreshold.Text = "CheckThreshold";
            this.btnCheckThreshold.UseVisualStyleBackColor = true;
            this.btnCheckThreshold.Click += new System.EventHandler(this.btnCheckThreshold_Click);
            // 
            // timerResetDeclareFlag
            // 
            this.timerResetDeclareFlag.Enabled = true;
            this.timerResetDeclareFlag.Interval = 10000;
            this.timerResetDeclareFlag.Tick += new System.EventHandler(this.timerResetDeclareFlag_Tick);
            // 
            // timerRepeat
            // 
            this.timerRepeat.Enabled = true;
            this.timerRepeat.Interval = 30000;
            this.timerRepeat.Tick += new System.EventHandler(this.timerRepeat_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(987, 472);
            this.Controls.Add(this.btnCheckThreshold);
            this.Controls.Add(this.btnAliveDeclare);
            this.Controls.Add(this.btnCalc);
            this.Controls.Add(this.btnReadcfg);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.btnFresh);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dgvDBStatus)).EndInit();
            this.tabControl1.ResumeLayout(false);
            this.tabPage1.ResumeLayout(false);
            this.tabPage2.ResumeLayout(false);
            this.tabPage2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCfg)).EndInit();
            this.tabPage3.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dgvCalc)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvDBStatus;
        private System.Windows.Forms.Button btnFresh;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.DataGridView dgvCfg;
        private System.Windows.Forms.TabPage tabPage3;
        private System.Windows.Forms.DataGridView dgvCalc;
        private System.Windows.Forms.Button btnReadcfg;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label lblAlarmInterval;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label lblFreshDataTableTime;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label lblAliveDeclareTime;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label lblMailAliveTo;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label lblMailFrom;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label lblMailSmtp;
        private System.Windows.Forms.Button btnCalc;
        private System.Windows.Forms.Button btnAliveDeclare;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblMailFromName;
        private System.Windows.Forms.Button btnCheckThreshold;
        private System.Windows.Forms.Timer timerResetDeclareFlag;
        private System.Windows.Forms.Timer timerRepeat;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label lblMailAlarmTo;
    }
}

