/*********************************************************************************
 *
 * Copyright (c) 2017 Josef Adamsson, Denise Härnström
 *
 * Inviwo - Interactive Visualization Workshop
 *
 * Copyright (c) 2017 Inviwo Foundation
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 *********************************************************************************/
 /*
  *   Alterations to this file by Abdullatif Ismail
  *
  *   To the extent possible under law, the person who associated CC0
  *   with the alterations to this file has waived all copyright and
  *   related or neighboring rights to the alterations made to this file.
  *
  *   You should have received a copy of the CC0 legalcode along with
  *   this work.  If not, see
  *   <http://creativecommons.org/publicdomain/zero/1.0/>.
  */

#ifndef IVW_STRUCTUREMESH_H
#define IVW_STRUCTUREMESH_H

#include <modules/crystalvisualization/crystalvisualizationmoduledefine.h>
#include <inviwo/core/common/inviwo.h>
#include <inviwo/core/processors/processor.h>
#include <inviwo/core/properties/ordinalproperty.h>
#include <inviwo/core/properties/boolproperty.h>
#include <inviwo/core/ports/meshport.h>
#include <inviwo/core/datastructures/buffer/bufferramprecision.h>
#include <inviwo/core/interaction/pickingmapper.h>
#include <modules/crystalvisualization/properties/intvectorproperty.h>

namespace inviwo {

/** \docpage{org.inviwo.StructureMesh, Structure Mesh}
 * ![](org.inviwo.StructureMesh.png?classIdentifier=org.inviwo.StructureMesh)
 * Explanation of how to use the processor.
 *
 * ### Inports
 *   * __<Inport1>__ <description>.
 *
 * ### Outports
 *   * __<Outport1>__ <description>.
 *
 * ### Properties
 *   * __<Prop1>__ <description>.
 *   * __<Prop2>__ <description>
 */


/**
 * \class StructureMesh
 * \brief VERY_BRIEFLY_DESCRIBE_THE_PROCESSOR
 * DESCRIBE_THE_PROCESSOR_FROM_A_DEVELOPER_PERSPECTIVE
 */
class IVW_MODULE_CRYSTALVISUALIZATION_API StructureMesh : public Processor {
public:
    StructureMesh();
    virtual ~StructureMesh() = default;

    virtual void process() override;

    virtual const ProcessorInfo getProcessorInfo() const override;
    static const ProcessorInfo processorInfo_;
private:
    void handlePicking(PickingEvent* p);

    DataInport<std::vector<vec3>, 0> structure_;
    MeshOutport mesh_;
    FloatProperty scalingFactor_;
    FloatMat3Property basis_;
    BoolProperty fullMesh_;
    BoolProperty animation_;
    IntProperty timestep_;
    std::vector<std::unique_ptr<FloatVec4Property>> colors_;
    std::vector<std::unique_ptr<FloatProperty>> radii_;
    std::vector<std::unique_ptr<IntProperty>> num_;
    std::shared_ptr<BufferRAMPrecision<vec4>> colorRAM_;
    std::shared_ptr<BufferRAMPrecision<vec3>> vertexRAM_;
    std::shared_ptr<BufferRAMPrecision<float>> radiiRAM_;
    BoolProperty enablePicking_;
    PickingMapper spherePicking_;
    IntSizeTProperty pickedIndex_;
};

} // namespace

#endif // IVW_STRUCTUREMESH_H
