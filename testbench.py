import cocotb
from cocotb.triggers import Timer
import random
import json
import wavedrom

mytimestamp = 1
Input = []

def TransformContinousString(s):
    transformed_str = ""
    for i in range(len(s)-1, 0, -1):
        if s[i] == s[i-1]:
            transformed_str = "." + transformed_str
        else:
            transformed_str = s[i] + transformed_str
    transformed_str = s[0] + transformed_str
    return transformed_str


@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 10

    # input driving
    dut.a.value = A
    dut.b.value = B

    await Timer(mytimestamp, units='ns')

    # assert dut.sum.value == A + \
    #     B, f"Adder result is incorrect: {dut.X.value} != 15"


@cocotb.test()
async def adder_randomised_test(dut):
    data = {'signal1': [], 'signal2': []}
    myoutput = []
    myInput1 = []
    myInput2 = []
    Exp_output = []
    """Test for adding 2 random numbers multiple times"""
    timeString = ""
    equalString = ""
    Mismatch_string = ""
    for i in range(15):
        if i > 0:

            timeString += "."
        equalString += "="
        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B
        myInput1.append(int(A))
        myInput2.append(int(B))
        Exp_output.append(int(A+B))
        await Timer(2, units='ns')
        # print(dut.sum.value,type(dut.sum.value),"\n")
        myoutput.append(int(dut.sum.value))
        if (int(dut.sum.value) == int(A+B)):
            Mismatch_string+='0'
           
        else:
            Mismatch_string+='1'
        print(Mismatch_string)
        data['signal1'].append([int(dut.a.value), int(dut.b.value)])
        data['signal2'].append(int(dut.sum.value))

        # myInput=myInput+dut.sum.value+" "
        # dut._log.info(
        #     f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        # assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
        #     A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
    json_data = json.dumps(data)
    print(json_data)
    with open("data.json", "w") as f:
        json.dump(data, f)
    print(myInput1, myInput2, myoutput, dut)

    # wd = waveDrom()
    s = " "
    Input1_string = s.join([str(elem) for elem in myInput1])
    Input2_String = s.join([str(elem) for elem in myInput2])
    Output_String = s.join([str(elem) for elem in myoutput])
    Exp_output_String = s.join([str(elem) for elem in Exp_output])
    Mismatch_string=TransformContinousString(Mismatch_string)
    print(equalString, timeString)
   # print(Input1_string,"\n",Input2_String,"\n",Output_String)
    data = {
        "signal": [
            {"name": "Clk", "wave": "P"+timeString},
            {"name": "Signal1",  "wave": equalString, "data": Input1_string},
            {"name": "Signal2",  "wave": equalString, "data": Input2_String},
            {"name": "Output",  "wave": equalString, "data": Output_String},
            {"name": "Exp_Output",  "wave": equalString, "data": Exp_output_String},
            {"name": "Mismatch",  "wave": Mismatch_string }




        ]
    }
    data_str = json.dumps(data)
    svg = wavedrom.render(data_str)
    svg.saveas("demo1.png")